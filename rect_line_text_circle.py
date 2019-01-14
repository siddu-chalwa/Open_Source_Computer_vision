import cv2
import numpy

#circle, line, text, rectangle drawing

backg = cv2.imread('me.jpg')


#circle
cv2.circle(backg, (150, 130), 90, (255, 255, 255), 3)
cv2.circle(backg, (350, 130), 90, (255, 255, 255), 3)
cv2.putText(backg, 'R', (165, 160), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 255, 255), 3, cv2.LINE_8)
cv2.putText(backg, 'C', (365, 160), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 255, 255), 3, cv2.LINE_8)

#line
cv2.line(backg, (175, 250), (325, 250), (255, 255, 255), 5)

#rectangle
cv2.rectangle(backg, (60, 300), (440, 450), (255, 255, 255), 5)
cv2.putText(backg, 'Siddu Chalwa', (65, 390), cv2.FONT_HERSHEY_DUPLEX, 1.7, (255, 255, 255), 5, cv2.LINE_8)
backg = cv2.resize(backg, (700, 500))
cv2.imshow('all_drawing', backg)
k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('all_drawing.jpg', backg)
    cv2.destroyAllWindows()

