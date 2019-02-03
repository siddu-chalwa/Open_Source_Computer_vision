import numpy as np
import cv2

# finction related to object tracking related functionalitu
class ObjectTracking(object):
    def __init__(self, scaling_factor = 0.5):
        # initialize video capture object
        self.cap = cv2.VideoCapture(0)

        # capture the frame
        _, self.frame = self.cap.read()

        # scaling factor for captured frame
        self.scaling_factor = scaling_factor

        # resize the frame
        self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA)

        # create a window tp display frame
        cv2.namedWindow('Object tracker')

        # set mouse callback function to track the mouse
        cv2.setMouseCallback('object tracker', self.mouse_event)

        # initial variable related to rectangular region selection
        self.selection = None

        # initial variable related to starting position
        self.drag_start = None

        # initial variable related to state of tracking
        self.tracking_state = 0


    # define for mouse tracking event
    def mouse_event(self, event, x, y, flags, param):
        # convert x and y coordinates into 16-bit numpy integers
        x, y = np.int16([x, y])

        # check if a mouse button down has occured
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
            self.tracking_state = None

        # check if the user start selecting
        if self.drag_start:
            if flags & cv2.EVENT_FLAG_LBUTTON:
                # extract the dimension of the frame
                h, w = self.frame.shape[:2]

                # get the initial position
                x1, y1 = self.drag_start

                # get max and min value
                x0, y0 = np.maximum(0, np.minimum([x1, y1], [x, y]))
                x1, y1 = np.minimum([w, h], np.maximum([x1, y1], [x, y]))

                # reset the selectoin variable
                self.selection = None

                # finilize the rectangular selection
                if x1-x0 > 0 and y1-y0>0 :
                    self.selection = (x0, y0, x1, y1)

                else:
                    # if selection is done
                    self.drag_start = None
                    if self.selection is not None:
                        self.tracking_state = 1

    # method to start tracking the object
    def start_tracking(self):
        # iterate until the esc
        while True:
            # capture frame from webcam
            _, self.frame = self.cap.read()

            # resize the input frame
            self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA)

            # create a copy of frame, it is done because as we do hsv operation it will chaneg the ogiginal image prpperty
            vis = self.frame.copy()

            # convert to HSV model
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # create mask based on predefined thresholds
            mask = cv2.inRange(hsv, np.array((0., 60., 32.,)), np.array(100., 255., 255.))

            # check if the user had selected the region
            if self.selection:
                # extract the coordinate of the selected rectangle
                x0, y0, x1, y1 = self.selection

                # extract the tracking window
                self.tracking_window = (x0, y0, x1-x0, y1-y0)

                # extract the region of interst
                hsv_roi = hsv[y0:y1, x0:x1]
                mask_roi = mask[y0:y1, x0:x1]

                # compute the hostogram of the regoin
                hist = cv2.calcHist([hsv_roi], [0], mask_roi, [16], [0, 100])

                # normalize the reshape the histogram
                cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
                self.hist = hist.reshape(-1)

                # extract ROi from frame
                vis_roi = vis[y0:y1, x0:x1]

                # compute image negative
                cv2.bitwise_not(vis_roi, vis_roi)
                vis[mask == 0] = 0

            # check if the system is in the tracking mode
            if self.tracking_state == 1:
                # reset the selection variable
                self.selection = None
                
                # compute the histogram back projection
                hsv_backproj = cv2.calcBackProject([hsv], [0], self.hist, [0, 180], 1)

                # compute bitwise and between histogram backprojection and mask
                hsv_backproj &= mask

                # define termination criteria for the tracker
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

                # apply camshift
                track_box, self.track_window = cv.CamShift(hsv_backproj, self.track_window, term_crit)

                cv2.ellipse(vis, track_box, (0, 0, 255), 2)

            # show output live video
            cv2.imshow('object tracker', vis)

            # stop if esc
            c = cv2.waitKey(5)
            if c == 27:
                break

        cv2.destroyAllWindows()


if __name__ == '__main__':
    ObjectTracking().start_tracking()
