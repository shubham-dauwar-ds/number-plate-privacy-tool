from ultralytics import YOLO

class PlateDetector:
    def __init__(self, model_path="models/plate_model.pt"):
        self.model = YOLO(model_path)

    def detect_plate(self, image_path):

        results = self.model(image_path)
        boxes = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))

        return boxes
