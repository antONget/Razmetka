import cv2
import numpy as np

img=cv2.imread('101_0000.png')
crop_img =None
x_crop = []
y_crop = []
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):

    if event == cv2.EVENT_RBUTTONDOWN:
        x_crop.append(x)
        y_crop.append(y)
        if len(x_crop)==2:
            print(x_crop[0], x_crop[1])
            print(y_crop[0], y_crop[1])
            crop_img = img[y_crop[0]:y_crop[1], 0:511]
            # Show image
            cv2.imshow("image", crop_img)

    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print(x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0,0,0), thickness = 1)
        # cv2.imshow("image", crop_img)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(0)&0xFF==27:
        break
cv2.destroyAllWindows()