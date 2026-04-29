# 🖼️ Image Restoration Project using OpenCV

## 📌 Project Title

**Old Image Restoration using Image Processing Techniques**

---

# 📖 Project Description

This project restores old or damaged images using basic image processing techniques.
It performs **denoising, sharpening, and upscaling** to improve image quality.

The system takes an input image (`sample.jpg`) and produces an enhanced version (`enhanced_sample.jpg`).

---

# 🎯 Objectives

* Remove noise from old images
* Improve image sharpness
* Increase image resolution
* Generate an enhanced output image
* Learn practical image processing using OpenCV

---

# 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **NumPy**

---

# 📦 Required Libraries

Install required libraries before running the project.

```bash
pip install opencv-python numpy
```

---

# 📂 Project Folder Structure

```
ImageProcessingLab/
│
├── imageproject.py
├── sample.jpg
├── enhanced_sample.jpg   (generated after running)
├── README.md
```

---

# ⚙️ How the Project Works

The project performs the following steps:

## Step 1 — Load Image

Loads the input image (`sample.jpg`) using OpenCV.

## Step 2 — Denoising

Removes noise using **Non-Local Means Denoising**.

Function Used:

```
cv2.fastNlMeansDenoisingColored()
```

## Step 3 — Sharpening

Improves edges using a sharpening filter kernel.

## Step 4 — Upscaling

Increases image resolution using bicubic interpolation.

Function Used:

```
cv2.resize()
```

## Step 5 — Save Output

Final enhanced image is saved as:

```
enhanced_sample.jpg
```

---

# ▶️ How to Run the Project

Follow these steps:

## Step 1

Place your input image:

```
sample.jpg
```

in the project folder.

## Step 2

Run the Python script:

```bash
python imageproject.py
```

## Step 3

Output image will be created:

```
enhanced_sample.jpg
```

---

# 📥 Input

```
sample.jpg
```

Any old or noisy image can be used.

---

# 📤 Output

```
enhanced_sample.jpg
```

Enhanced version of the input image.

---

# 🧠 Functions Used in Code

## load_image(path)

Loads image from given path.

## denoise(img)

Removes noise from image.

## sharpen(img)

Sharpens image edges.

## upscale(img)

Increases image resolution.

## restore_image(input_path)

Runs the full restoration pipeline.

---

# ⚠️ Common Errors & Fixes

## Error:

```
Image not found
```

### Fix:

Make sure:

```
sample.jpg
```

exists in the same folder.

---

## Error:

```
Type of input image should be CV_8UC3
```

### Fix:

Check that image is loaded correctly.

---

# 📌 Applications

* Old photo restoration
* Image enhancement
* Digital image processing learning
* Academic lab experiments
* Basic restoration systems

---

# 🚀 Future Improvements

* Add colorization feature
* Use deep learning models
* Face enhancement
* Scratch removal
* GUI interface

---

# 👨‍💻 Author

**Student Image Processing Project**

---

# 📚 Conclusion

This project demonstrates how basic image processing techniques like denoising, sharpening, and upscaling can significantly improve the quality of old images using Python and OpenCV.
