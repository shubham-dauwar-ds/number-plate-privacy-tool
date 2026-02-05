from detector import PlateDetector
from image_processing import blur_plate
import os

# Initialize the detector with your YOLO plate model
detector = PlateDetector()

# Folders
input_folder = "data/input_images"
output_folder = "data/output_images"

# Loop over all images in input folder
for img_file in os.listdir(input_folder):
    # Skip hidden files/folders (like .ipynb_checkpoints)
    if img_file.startswith("."):
        continue

    # Full path to input image
    image_path = os.path.join(input_folder, img_file)

    # Detect plates (returns list of boxes)
    boxes = detector.detect_plate(image_path)

    # Full path to save output image
    save_path = os.path.join(output_folder, img_file)

    # Apply blur to detected plates and save
    blur_plate(image_path, boxes, save_path)

    print(f"Processed {img_file} → {len(boxes)} plates blurred")
