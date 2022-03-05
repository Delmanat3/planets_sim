from turtle import width
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame= cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    #x marks de spot
    # image=cv2.line(frame,(0,0),(width,height),(255,0,0),10)#top left is 0,0 cuz fuck cartiesian i gues
    # image1=cv2.line(image,(0,height),(width,0),(255,0,0),10)#top left is 0,0 cuz fuck cartiesian i gues
    imageRec=cv2.rectangle(frame, (0,0),(200,200),(128,128,128),10 )#rectangle
    imageRec=cv2.circle(frame,(300,300),60 , (0,0,255),-1)
# four side by sides
    # image=np.zeros(frame.shape, np.uint8)
    # smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    # # half height half width for resized img 
    # # top left 
    # image[:height//2, : width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    # #bottom left
    # image[height//2:, : width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    #  # top right
    # image[:height//2,  width//2 :] = smaller_frame
    # # bottome right
    # image[height//2:,  width//2 :] = smaller_frame

    cv2.imshow('frame',imageRec)

    if cv2.waitKey(1)== ord('q'):
        break


cap.release()
cv2.destroyAllWindows()