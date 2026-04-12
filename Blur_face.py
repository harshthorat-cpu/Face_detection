import cv2 as cv
face_cascade = cv.CascadeClassifier('haar_face.xml')
webcam = cv.VideoCapture(0)
while True:
     _img = webcam.read()[1]
     gray = cv.cvtColor(_img,cv.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray,1.1,4)
     
     
     for(x,y,w,h) in faces:
        face_roi = _img[y:y+h, x:x+w]
        blurred = cv.GaussianBlur(face_roi,(151,151),0)
        _img[y:y+h, x:x+w] = blurred
        cv.imshow('face',_img)
     
     key = cv.waitKey(30) & 0xff
     if key == 27:
          

      break
webcam.release()
cv.destroyAllWindows()
