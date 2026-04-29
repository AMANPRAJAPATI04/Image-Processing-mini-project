import cv2
import numpy as np
import os

# -----------------------------
# STEP 1: Load Image
# -----------------------------
def load_image(path):

    if not os.path.exists(path):
        print("Error: Image file not found ->", path)
        exit()

    img = cv2.imread(path)

    if img is None:
        print("Error: Unable to load image.")
        exit()

    return img

# -----------------------------
# STEP 2: Denoising (Fixed)
# -----------------------------
def denoise(img):

    # Convert grayscale to color if needed
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Ensure uint8 format
    if img.dtype != np.uint8:
        img = img.astype(np.uint8)

    denoised = cv2.fastNlMeansDenoisingColored(
        img,
        None,
        10,
        10,
        7,
        21
    )

    return denoised


# -----------------------------
# STEP 3: Sharpening
# -----------------------------
def sharpen(img):

    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharp = cv2.filter2D(img, -1, kernel)

    return sharp


# -----------------------------
# STEP 4: Super Resolution
# -----------------------------
def upscale(img):

    upscaled = cv2.resize(
        img,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    return upscaled


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def restore_image(input_path):

    print("Loading Image...")
    img = load_image(input_path)

    print("Denoising...")
    denoised = denoise(img)

    print("Sharpening...")
    sharp = sharpen(denoised)

    print("Upscaling...")
    upscaled = upscale(sharp)

    # Save output
    output_path = "enhanced_sample.jpg"
    cv2.imwrite(output_path, upscaled)

    print("Restoration Completed!")
    print("Saved as:", output_path)


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":

    restore_image("sample.jpg")