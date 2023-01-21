# from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor

# import cv2

# model = YOLO("yolov8m.pt")

# results = model.predict(source="rtsp://admin:team6009@192.168.0.104:554/cam/realmonitor?channel=1&subtype=0", show = True)
# print(results)

from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("yolov8m.pt")

results = model.predict(source="rtsp://admin:team6009@192.168.0.104:554/cam/realmonitor?channel=1&subtype=0", show = True)
print(results)