import cv2
import  numpy as np

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


drawing = False              # false as long as mouse is not pressed
mode = True                     # if true draw
ix, iy = -1, -1

img = cv2.imread('me.jpg')
cv2.namedWindow('mouse_draw')
cv2.setMouseCallback('mouse_draw', draw_circle)

while(1):
    cv2.imshow('mouse_draw', img)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        mode = not mode
    elif cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

