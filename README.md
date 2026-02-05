# Number Plate Privacy Tool

This project detects and hides number plates in images using PyTorch and OpenCV.

## Project Structure

- `app.py` : Main script to process images
- `detector.py` : Number plate detection logic
- `image_processing.py` : Functions to blur or mask plates
- `models/plate_model.pt` : Pretrained PyTorch model
- `data/input_images/` : Folder for original images
- `data/output_images/` : Folder for processed images
- `requirements.txt` : Project dependencies

## Usage

1. Place images in `data/input_images/`.
2. Run `app.py`:

```bash
python app.py
