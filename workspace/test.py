# import module
import cv2
import schedule
from playsound import playsound
from gtts import gTTS

threshold = 5

def alarm():
    text = "현재 " + str(len(faces)) + "명 있습니다."
    print(text)
    tts = gTTS(text=text, lang='ko')
    filename = 'tts.mp3'
    tts.save(filename)
    playsound(filename)

schedule.every(10).seconds.do(alarm)

# setting up the haar cascade classifiers from the opencv installation
face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_eye.xml')

webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    # cv2.imshow("frame", frame)

    # img = cv2.imread('2.JPG')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # search for faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # for each face, detect eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
    if len(faces) >= threshold:
        playsound("BeepBeep.mp3")

    # displaying the image
    cv2.imshow('Count People', frame)
    schedule.run_pending()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
