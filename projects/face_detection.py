import cv2

from datetime import datetime
from config import CASCADE_CLASSIFIER, TEST_IMG, OUTPUT_IMG

def detect_face():
    face_cascade = cv2.CascadeClassifier(CASCADE_CLASSIFIER)
    img = cv2.imread(TEST_IMG)
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_scale, 1.1, 4)
    timestamp = datetime.now()

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 4)

    cv2.imshow('Face Detected', img)
    cv2.waitKey()

    cv2.imwrite(f'{OUTPUT_IMG}-{timestamp}.jpg', img)

if __name__ == "__main__":
    detect_face()
