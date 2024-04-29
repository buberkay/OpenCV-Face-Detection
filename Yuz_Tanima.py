# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:16:44 2024

@author: 90553
"""

import cv2

cam = cv2.VideoCapture('data/video_00.mp4')
fps = cam.get(cv2.CAP_PROP_FPS)

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cam.read()
    if ret==True:
        frame = cv2.resize(frame, (500, 500 ))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    face = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)
    
    # print(face)
    
    for(x,y,w,h) in face:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), thickness = 2)
    cv2.imshow("Goruntu", frame)
    
    if ( cv2.waitKey(10) & 0XFF == ord('q') ) :
        break 
cam.release()
cv2.destroyAllWindows()