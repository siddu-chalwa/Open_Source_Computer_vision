import cv2
import numpy as np

# define function to get frame from camera

def get_frame(cap, scaling_factor):

    # read the current frame from the video capture object
    frmae = cap.read()

    # resize img
    frame = cv2.resize(frmae, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__== '__main__':

    # define video capture object
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    # keep reading the frame from camera until user hit esc

    while(1):

        frame = get_frame(cap, scaling_factor)

        # convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of skin color
        lower = np.array([0, 70, 60])
        upper = np.array(50, 150, 255)

        #thrishold to get only skin color
        mask = cv2.inRange(hsv, lower, upper)

        img_bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)

        img_median_blurring = cv2.medianBlur(img_bitwise_and, 5)

        cv2.imshow('Input', frame)
        cv2.imshow('Output', img_median_blurring)

        c= cv2.waitKey(5)
        if c == 27:
            break

cv2.destroyAllWindows()
