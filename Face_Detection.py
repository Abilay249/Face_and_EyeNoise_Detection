import cv2

face_info = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_info = cv2.CascadeClassifier('haarcascade_eye.xml')

#img = cv2.imread('1.jpg') // you can run with image detection

webcam = cv2.VideoCapture(0)

while True:

    succesful_frame_read, frame = webcam.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coord = face_info.detectMultiScale(gray_image)
    eye_coord = eye_info.detectMultiScale(gray_image)

    for(x, y, w, h) in face_coord:
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 200, 0), 5)

    for(x, y, w, h) in eye_coord:
        cv2.rectangle(frame, (x, y), (x+w,y+h), (65, 55, 0), 5)

    cv2.imshow('Abylay Face Detector', frame)

    key = cv2.waitKey(1)

    #Press Q to to quit
    if key ==81 or key ==113:
        break

#Release Video Capture
webcam.realise()

#face_coord = face_info.detectMultiScale(gray_image)

#for(x, y, w, h) in face_coord:
    #cv2.rectangle(img, (x, y), (x+w,y+h), (randrange(255), randrange(255), randrange(255)), 7)

#print(face_coord)

#cv2.imshow('Abylay', img)

#cv2.waitKey()

#print('Hello')