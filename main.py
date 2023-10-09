from ultralytics import YOLO
from dotenv import load_dotenv
import os

load_dotenv()

root_dir = os.environ.get("root_dir")
# print(f"Root directory: {root_dir}")

model = YOLO("yolov8n-cls.pt")

def train_YOLO(model, dataset_dir):
    '''Train YOLOv8 model on custom dataset stored in directory: dataset_dir'''

    print("YOLO training now...")
    results = model.train(data=dataset_dir, epochs=16, imgsz=224)

    return results