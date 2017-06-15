# -*- coding: utf-8 -*-
# detect face
 
import sys
import os
import cv2 as cv
from glob import glob
 
def detect(imagefilename, cascadefilename):
    srcimg = cv.imread(imagefilename)
    print srcimg
    if srcimg is None:
        print('cannot load image')
        sys.exit(-1)
    dstimg = srcimg.copy()
    cascade = cv.CascadeClassifier(cascadefilename)
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    objects = cascade.detectMultiScale(srcimg, 1.1, 3)
    for (x, y, w, h) in objects:
        # print(x, y, w, h)
        # dstimg = dstimg[y:y+h, x:x+w]
        cv.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return dstimg
 
if __name__ == '__main__':

    path = "hagiwaralabo.jpg"
    result = detect(path, 'haarcascade_frontalface_alt.xml')
    cv.imwrite('output2.png', result)
    