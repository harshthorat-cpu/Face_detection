import cv2 as cv
face_cascade = cv.CascadeClassifier('haar_face.xml')
webcam = cv.VideoCapture(0)
while True:
     _img = webcam.read()[1]
     gray = cv.cvtColor(_img,cv.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray,1.1,4)
     for(x,y,w,h) in faces:
         cv.rectangle(_img,(x,y),(x+w,y+h),(255,0,0),2)
         cv.imshow('face',_img)
     
         key = cv.waitKey(30) & 0xff
         if key == 27:
          

          break
webcam.release()
cv.destroyAllWindows()