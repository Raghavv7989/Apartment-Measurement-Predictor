from config import FLOOR_HEIGHT_METERS, PIXELS_PER_METER

def analyze_bbox(w, h):
    length_px = max(w, h)
    width_px  = min(w, h)
    length_m  = length_px / PIXELS_PER_METER
    width_m   = width_px / PIXELS_PER_METER
    return length_m, width_m, length_px, width_px

def estimate_floor_count(length_m):
    if FLOOR_HEIGHT_METERS <= 0:
        return 1
    count = int(round(length_m / FLOOR_HEIGHT_METERS))
    return max(1, min(count, 150))
