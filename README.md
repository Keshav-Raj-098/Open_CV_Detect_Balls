# 🎯 Red and Blue Ball Detection using OpenCV

This project detects **red and blue-colored balls** in an image and outputs their **left-to-right order**. It's built using Python and OpenCV, and is designed for specific image constraints to ensure accurate detection.

---

## 🧠 Purpose

The goal of this project is to identify and distinguish **red** and **blue balls** in an image, determining their **order from left to right**. This task is useful in basic color detection workflows, computer vision learning, and object tracking scenarios.

---

## 📦 Dependencies

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  

Install dependencies using:
```bash
pip install opencv-python numpy
```

---

## ⚙️ How to Use

1. Place your image file in the **same folder** as the Python script.
2. In the script, replace the image name in the following line:
   ```python
   img = cv2.imread("your_image.jpg")
   ```
3. Run the script:
   ```bash
   python detect_balls.py
   ```

---

## 📌 Assumptions & Constraints

This program works under the following image conditions:

- Exactly **3 balls** are present in the image.
- Each ball must be either **red** or **blue**.
- Balls must **not overlap** or be **partially out of frame**.
- The background must **not contain red or blue shades**.

---

## 🎨 Color Range Logic

The detection logic is based on the **HSV color space**, which is more robust for color segmentation than RGB.

- Custom HSV ranges for **Red** and **Blue** have been defined based on practical testing.
- These ranges should detect most common shades of red and blue.

---

## ✅ Testing

- The program has been successfully tested on **10+ image samples** that meet the above constraints.
- All test cases showed correct ordering and classification of the balls.

---
