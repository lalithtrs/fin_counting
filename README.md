## **Fin Detection and Counting**

### **Introduction**

This document outlines the steps and methods employed to detect and count circular objects within an image. The process involves image preprocessing, thresholding, contour detection, and filtering to identify and quantify the desired circles.

### **Methods and Approach**

#### **1. Image Preprocessing**

* **Grayscale Conversion:** The original image is converted to grayscale to simplify subsequent processing steps.
* **Gaussian Blurring:** A Gaussian blur is applied to reduce noise and enhance edge detection.
* **Resize (Optional):** If necessary, the image can be resized to a specific resolution for faster processing or to accommodate computational constraints.

#### **2. Thresholding**
* **Adaptive Thresholding:** Adaptive thresholding is used to create a binary image, separating foreground objects (circles) from the background. The `cv2.adaptiveThreshold` function with `ADAPTIVE_THRESH_GAUSSIAN_C` method is employed.
* **Thresholding Parameters:** The thresholding parameters (block size, constant) are adjusted to optimize the separation of circular objects from the background.

#### **3. Contour Detection**
* **Contour Finding:** The `cv2.findContours` function is used to detect contours within the thresholded image.
* **Contour Filtering:** The detected contours are filtered based on specific criteria to identify circular objects:
    - **Aspect Ratio:** The ratio of width to height is checked to ensure objects are approximately circular.
    - **Area:** The area of the contour is evaluated to filter out objects that are too small or too large.
    - **Enclosing Circle Radius:** The radius of the minimum enclosing circle is compared to a threshold to further refine the selection of circular objects.

#### **4. Circle Counting**
* **Iteration and Filtering:** Each contour is examined, and those meeting the specified criteria are counted as circular objects.
* **Circle Drawing:** The detected circles can be visualized by drawing circles on the original image.

#### **5. Results**
* **Output:** We can pass a directory images to the code, it will preprocess and count the number of circles in the image and upadte it int he output folder as results.