import cv2 
im_g = cv2.imread("smallgray.png",0)
arr = cv2.imwrite("newsmallgray.png",im_g)
print(arr)