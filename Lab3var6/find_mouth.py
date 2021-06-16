import logging
import logging.config

import cv2
import numpy as np


class FindMouth:

    def __init__(self, file_path=None):
        self.path = file_path

    def find_mouth(self):
        mouth_cascade_path = "haarcascade_smile.xml"
        mouth_cascade = cv2.CascadeClassifier(mouth_cascade_path)
        font = cv2.FONT_HERSHEY_SIMPLEX
        gray = cv2.cvtColor(self, cv2.COLOR_BGR2GRAY)

        mouths = mouth_cascade.detectMultiScale(
            gray,
            scaleFactor=1.7,
            minNeighbors=40,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x_smile, y_smile, w_smile, h_smile) in mouths:
            cv2.rectangle(self, (x_smile, y_smile), (x_smile + w_smile, y_smile + h_smile), (255, 0, 0), 2)
            cv2.putText(self, 'Smile', (x_smile, y_smile), font, 1, (0, 255, 0), 1)


    def image_find_mouth(self: str):
        image = cv2.imread(self)

        FindMouth.find_mouth(image)

        cv2.imshow("Image", image)
        logging.info('csv window opened')
        cv2.imwrite('result_by_open.jpg', image)
        logging.info('picture saved')
        cv2.waitKey()

    @staticmethod
    def video_find_mouth():
        cv2.namedWindow("preview")
        video_capture = cv2.VideoCapture(0)
        logging.info('csv video capture')
        ret, image = video_capture.read()
        while True:
            if image is not None:
                ret, image = video_capture.read()

                FindMouth.find_mouth(image)

                cv2.imshow("Video", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        logging.info('csv window destroyed')
        cv2.destroyAllWindows()

