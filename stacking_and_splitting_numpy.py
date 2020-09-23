import cv2 
import numpy
im_g = cv2.imread("smallgray.png",0)
imsh = numpy.hstack((im_g,im_g)) #stacking horizontally. here we stack only 2 im_g
imsv = numpy.vstack((im_g,im_g))
lsth = numpy.hsplit(imsh,10)
lstv = numpy.vsplit(imsv,2)
m = lstv[0]
#print(imsh)
#print(imsv)
#print(lsth)
#print(lstv)
print(m)