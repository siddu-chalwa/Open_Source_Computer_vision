import cv2
import numpy as np

# define function to track object
def start_tracking():
    # initialize the video capture object
    cap = cv2.VideoCapture(0)

    # define the scaling factor
    scaling_factor = 0.5

    # no. of frames to track
    num_frames_to_track = 5

    # skippping factor
    num_frames_jump = 2

    # initialize the variable
    tracking_paths = []
    frame_index = 0

    # define tracking parameter
    tracking_params = dict(winSize = (11, 11), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # iterate untill the user hits the esc
    while True:
        # capture the current frame
        _, frame = cap.read()

        # resize the frame
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        # convert to gray scale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a copy of frame
        output_img = frame.copy()

        if len(tracking_paths) > 0:
            # get image
            prev_img, current_img = prev_gray, frame_gray

            # organize the feature points
            feature_points_0 = np.float32([tp[-1] for tp in tracking_paths]).reshape(-1, 1, 2)

            # compute optical flow
            feature_points_1, _, _ =  cv2.calcOpticalFlowPyrLK(prev_img, current_img, feature_points_0, None, **tracking_params)

            # compute reverse optical flow
            feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(prev_img, current_img, feature_points_1, None, **tracking_params)

            # compute the difference between forward and reverse optical flow
            diff_feature_points = abs(feature_points_0 - feature_points_0_rev).reshape(-1, 2).max(-1)

            # extract the good pointers
            good_pointers = diff_feature_points < 1

            # initialize variable
            new_tracking_paths = []

            # iterate through all the good feature points
            for tp, (x, y), good_pointers_flag in zip(tracking_paths, feature_points_1.reshape(-1, 2), good_pointers):
                # if flag is not true then continue
                if not good_pointers_flag:
                    continue

                # append the X and Y coordinate and check if its length greater than the threshold
                tp.append((x, y))
                if len(tp) > num_frames_to_track:
                    del tp[0]

                new_tracking_paths.append(tp)

                # draw a circle around the feature points
                cv2.circle(output_img, (x, y), 3, (0, 255, 0), -1)

            # update the tracking path
            tracking_paths = new_tracking_paths

            # draw lines
            cv2.polylines(output_img, [np.int32(tp) for tp in tracking_paths], False, (0, 150, 0))

        # go into this if condition after skipping the right numbers of frames
        if not frame_index % num_frames_jump:
            # creat the mask and draw the circles
            mask = np.zeros_like(frame_gray)
            mask[:] = 255
            for x, y in [np.int32(tp[-1]) for tp in tracking_paths]:
                cv2.circle(mask, (x, y), 6, 0, -1)

            # compute good features to track
            feature_points = cv2.goodFeaturesToTrack(frame_gray, mask=mask, maxCorners=500, qualityLevel=0.3, minDistance=7, blockSize=7)

            # check if feature points exist, if so, append them to the tracking paths
            if feature_points is not None:
                for x, y in np.float32(feature_points).reshape(-1, 2):
                    tracking_paths.append([x, y])
        # update variable
        frame_index += 1
        prev_gray = frame_gray

        # display output
        cv2.imshow('optical flow', output_img)

        # check if the user hit the esc
        c = cv2.waitKey(1)
        if c == 27:
            break

if __name__=='__main__':
    # start the tracker
    start_tracking()

    cv2.destroyAllWindows()

