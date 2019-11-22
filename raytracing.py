import numpy as np
import cv2
def createTestPNG(w,h):
    color=np.zeros([w,h,3])
    for i in range(w):
        for j in range(h):
            color[i][j]=[0.2*255,j/w*255,i/w*255]
    return color
cv2.imwrite('./test.png',createTestPNG(480,640))
