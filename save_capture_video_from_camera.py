import  numpy
import cv2

cap = cv2.VideoCapture('s_jobs.mp4')       # 0 --> camera  or file name
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('write_video.avi', fourcc, 20, (700, 500))    # 20 --> frames per sec and dimension

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

