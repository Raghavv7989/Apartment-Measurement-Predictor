import cv2
import numpy as np
from config import *

def draw_measurements(image, x, y, w, h, length_m, width_m, floor_count, sidebar_w=WINDOW_WIDTH):
    # Draw bounding box
    cv2.rectangle(image, (x, y), (x + w, y + h), COLOR_BBOX, 2)

    # Always treat length as the larger side
    length_px = max(w, h)
    width_px = min(w, h)

    # Draw vertical length line (blue): always left of building
    length_line_x = x - 10 if x - 10 > 0 else x + w + 10
    cv2.line(image, (length_line_x, y), (length_line_x, y + h), (255, 0, 0), 3)
    cv2.putText(image, f"Length: {length_m:.2f} m", (length_line_x + 12, y + 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Draw horizontal width line (yellow): always at base
    width_line_y = y + h + 10
    cv2.line(image, (x, width_line_y), (x + w, width_line_y), (0, 255, 255), 3)
    cv2.putText(image, f"Width: {width_m:.2f} m", (x + 10, width_line_y + 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Sidebar with measurements
    h_img, w_img = image.shape[:2]
    sidebar = np.full((h_img, sidebar_w, 3), COLOR_BG, dtype=np.uint8)
    y_pos = 40
    cv2.putText(sidebar, "MEASUREMENTS:", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLOR_TEXT, 2)
    y_pos += 60
    cv2.putText(sidebar, f"Length: {length_m:.2f} m", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLOR_TEXT, 2)
    y_pos += 60
    cv2.putText(sidebar, f"Width: {width_m:.2f} m", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLOR_TEXT, 2)
    y_pos += 60
    cv2.putText(sidebar, f"Floors: {floor_count}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLOR_TEXT, 2)

    return np.hstack((image, sidebar))
