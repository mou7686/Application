# 0 means grey scale and 1 means bgr i.e, blue-green-red scale
import cv2
im_g = cv2.imread("smallgray.png",0)
print(im_g)