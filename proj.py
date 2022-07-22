# author : shubham prasad 
# project given by devtown

import numpy as np
import cv2

video=cv2.VideoCapture("greenVideo.mp4")
image=cv2.imread("rungta-college.jpg")

while True:
    ret, frame = video.read()                   #ret returns the false if video file can not be read or if it is corrupted

    frame = cv2.resize(frame,(460,290))         #resize is used for resizing any image or any video
    image = cv2.resize(image,(460,290))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #cvtColor is used for converting type of color of any image or video
    
    low_green = np.array([32,194,132])
    upr_green = np.array([179,255,255])
    mask=cv2.inRange(hsv,low_green,upr_green)

    prefinal=cv2.bitwise_and(frame,frame,mask=mask)
    prefinal=frame-prefinal                           #subtracting masked image from the original image for preprefinal result

    final=np.where(prefinal==0,image,prefinal)        #all the black areas in the prefinal are valued as zero , and here we are changing the 0 with the image

    cv2.imshow("original",frame)
    cv2.imshow("video",mask)
    cv2.imshow("prefinal ",prefinal)
    cv2.imshow("final ",final)
    cv2.imshow("image",image)

    k=cv2.waitKey(1)                            #waitkey is used to take the input during run time of program and 1 specifies that only one character to be take as a input
    if(k==ord('q')):                            # 'q' is used to close all the open window and ord is used to change any word to its unicode
        break

video.release()                                 # release() function is used to free the memory acquired by any entity
cv2.destroyAllWindows()                         #destroyAllWindows() function closes all the ongoing tasks or window of the program
