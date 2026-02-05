import cv2

def blur_plate(image_path, boxes, save_path):
    """
    Blur regions in an image defined by bounding boxes.

    Parameters:
    - image_path: str, path to the input image
    - boxes: list of tuples, each tuple is (x1, y1, x2, y2)
    - save_path: str, path to save the blurred image
    """
    img = cv2.imread(image_path)

    for (x1, y1, x2, y2) in boxes:
        roi = img[y1:y2, x1:x2]  # region of interest
        blurred = cv2.GaussianBlur(roi, (25, 25), 30)
        img[y1:y2, x1:x2] = blurred

    cv2.imwrite(save_path, img)
