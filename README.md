# 🏙️ Skyscraper & Apartment Measurement Predictor

Automate rapid measurement of a building's real-world **height**, **width**, and **floor count** from a single image using Python + OpenCV!

---

## 📷 Example

![example](./images/example_apartment.jpg)

The system overlays:
- **Blue bar:** Length (height)
- **Yellow bar:** Width (base)
- **Metrics sidebar** with all numbers & estimated floors (using 3m per floor)

---

## Features

- 🏗️ **Automatic detection** of buildings from photos (front or angled views)
- 📏 **Length (height) and width calculation** from bounding box
- 🎯 **Accurate floor count** for apartments or towers (uses 3m/floor)
- 🟦 **Always-visible blue and yellow bars** overlayed on the building
- 📰 **Sidebar** for quick reading: length, width, and floors—all nicely spaced
- ⚡ **Fast and dependency-light:** Just Python, OpenCV, NumPy

---

## Installation

pip install opencv-python numpy
text

---

## Calibration

Edit `config.py`:
PIXELS_PER_METER = 1.75
text
- Calibrate PIXELS_PER_METER by measuring a known feature in the image or by matching measured floors to real floor count.

---

## Usage

python main.py your_apartment_photo.jpg
text

Output:  
- Shows the photo with visual overlays and sidebar with precise dimensions and estimated floors.

---

## Project Structure

skyscraper_measurement/
├── main.py
├── config.py
├── detector.py
├── visualizer.py
├── calibrator.py
├── helpers.py
└── requirements.txt
text

---

## How Floor Estimation Works

- The vertical length of the detected building is divided by **3 meters** to estimate floors.
- Easy to adjust for other building types (e.g., offices with taller floors).

---

## Example Output

MEASUREMENTS:
Length: 102.85 m
Width: 34.29 m
Floors: 34
text
Blue and yellow lines appear directly on the image for easy validation.

---

## License

MIT License © [Your Name]

---

## Acknowledgments

This tool was built for real-estate, architecture, and smart-city applications, or anyone who needs **fast floor/size analysis from imagery**.

---
