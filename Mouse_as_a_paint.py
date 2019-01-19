import cv2
import  numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (350, 200), 150, (255, 0, 0), -1)      # -1 --> color complete circle


events = [i for i in dir(cv2) if 'EVENT' in i]      # u will get the list of events for mouse
print(events)

img = cv2.imread('me.jpg')
cv2.namedWindow('mouse_circle')
cv2.setMouseCallback('mouse_circle', draw_circle)

while(1):
    img = cv2.resize(img, (700, 500))
    cv2.imshow('mouse_circle', img)
    if cv2.waitKey(20)&0xFF == 27:           # 27 --> esc
        break
cv2.destroyAllWindows()

