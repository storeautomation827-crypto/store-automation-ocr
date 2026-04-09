import os
import cv2
import numpy as np
from PIL import Image
import pytesseract


def rotate_image_bound(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos = abs(matrix[0, 0])
    sin = abs(matrix[0, 1])

    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    matrix[0, 2] += (new_w / 2) - center[0]
    matrix[1, 2] += (new_h / 2) - center[1]

    return cv2.warpAffine(
        image,
        matrix,
        (new_w, new_h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )


def estimate_skew_angle(binary_inv):
    coords = np.column_stack(np.where(binary_inv > 0))
    if len(coords) < 100:
        return 0.0

    rect = cv2.minAreaRect(coords)
    angle = rect[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    if abs(angle) > 15:
        return 0.0

    return angle


def crop_main_content(binary_inv, original_gray):
    contours, _ = cv2.findContours(binary_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return original_gray

    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)

    height, width = original_gray.shape[:2]
    if w < width * 0.3 or h < height * 0.3:
        return original_gray

    pad_x = int(w * 0.03)
    pad_y = int(h * 0.03)

    x1 = max(0, x - pad_x)
    y1 = max(0, y - pad_y)
    x2 = min(width, x + w + pad_x)
    y2 = min(height, y + h + pad_y)

    return original_gray[y1:y2, x1:x2]


def preprocess_with_opencv(image_path: str):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape[:2]
    if w > h:
        gray = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, binary = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    binary_inv = 255 - binary

    angle = estimate_skew_angle(binary_inv)
    rotated_gray = rotate_image_bound(gray, angle)

    rotated_blur = cv2.GaussianBlur(rotated_gray, (5, 5), 0)
    _, rotated_binary = cv2.threshold(
        rotated_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    rotated_binary_inv = 255 - rotated_binary

    cropped_gray = crop_main_content(rotated_binary_inv, rotated_gray)

    ch, cw = cropped_gray.shape[:2]
    scaled = cv2.resize(cropped_gray, (cw * 2, ch * 2), interpolation=cv2.INTER_CUBIC)

    _, final_binary = cv2.threshold(
        scaled, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return final_binary


def crop_regions(final_binary):
    height, width = final_binary.shape[:2]

    top_region = final_binary[
        int(height * 0.02):int(height * 0.28),
        int(width * 0.05):int(width * 0.95)
    ]

    sales_region = final_binary[
        int(height * 0.30):int(height * 0.62),
        int(width * 0.05):int(width * 0.78)
    ]

    return top_region, sales_region


def ocr_region(region, psm=6):
    pil_img = Image.fromarray(region)
    return pytesseract.image_to_string(
        pil_img,
        lang="jpn",
        config=f"--psm {psm}"
    )


def run_ocr(image_path: str) -> dict:
    final_binary = preprocess_with_opencv(image_path)
    top_region, sales_region = crop_regions(final_binary)

    top_text = ocr_region(top_region, psm=6)
    sales_text = ocr_region(sales_region, psm=6)

    return {
        "top_text": top_text,
        "sales_text": sales_text,
    }
