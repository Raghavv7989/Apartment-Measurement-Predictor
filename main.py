import sys
import cv2
from detector import detect_skyscraper
from helpers import analyze_bbox, estimate_floor_count
from visualizer import draw_measurements

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return
    path = sys.argv[1]
    image = cv2.imread(path)
    if image is None:
        print("Image not found or invalid")
        return
    res = detect_skyscraper(image)
    if res is None:
        print("No skyscraper detected")
        return
    x, y, w, h, _ = res
    length_m, width_m, length_px, width_px = analyze_bbox(w, h)
    floor_count = estimate_floor_count(length_m)
    annotated = draw_measurements(image.copy(), x, y, w, h, length_m, width_m, floor_count)
    cv2.imshow("Skyscraper Measurements", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
