import cv2
import keyboard

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

doggo = cv2.imread("doggo.png")

cap = cv2.VideoCapture(0)

blur_boolean = False

face_cover_boolean = False

while True:
    _, img = cap.read()

    if face_cover_boolean:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 3)
        for x, y, w, h in faces:
            resized_doggo = cv2.resize(doggo, (w, h))
            img[y:y+w, x:x+h] = resized_doggo

    if blur_boolean:
        img = cv2.blur(img, (10, 10))

    cv2.imshow('img', img)

    while keyboard.is_pressed('`'):
        pass

    k = cv2.waitKey(30) & 0xff

    if k == 98:
        blur_boolean = not blur_boolean
    if k == 102:
        face_cover_boolean = not face_cover_boolean
    if k == 27:
        break
