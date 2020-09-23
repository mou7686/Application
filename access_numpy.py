import cv2
im_g = cv2.imread("smallgray.png",0)
sl_ice = im_g[0:2,2:4]
particular_one_number = im_g[2,4]
#for row in im_g:
    #print(row)
#for column in im_g.T:
    #print(column)
for i in im_g.flat:
    print(i)
#print(im_g)
#print(sl_ice)
#print(particular_one_number)