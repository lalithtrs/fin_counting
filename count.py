import cv2
import os

def process_images_in_directory(directory, output):
    image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]  # Adjust file extension if needed
    image_files.sort()  # Sort image files for consistent numbering

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(directory, image_file)
        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,3)

        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        count = 0
        for c in cnts:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            ratio = w/h
            ((x, y), r) = cv2.minEnclosingCircle(c)
            if ratio > .86 and ratio < 1.20 and area > 50 and area < 120 and r < 7:
                cv2.circle(image, (int(x), int(y)), int(r), (36, 255, 12), -1)
                count += 1

        # Find circles
        circle_count = count

        # Add text to the image
        text = f"Circle Count: {circle_count}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (30, 120)  # Top-left corner coordinates
        fontScale = 5
        color = (255, 255, 255)  # White color
        thickness = 6
        cv2.putText(image, text, org, font, fontScale, color, thickness)

        print('Count: {}'.format(count))
        cv2.imwrite('result.jpg', image)
        cv2.waitKey()
        # Save the result with a numbered filename
        result_filename = f"result_{i+1}.jpg"
        result_path = os.path.join(output, result_filename)
        cv2.imwrite(result_path, image)

# Specify the directory containing your images
directory = "Images"

# Process the images
process_images_in_directory(directory=directory, output="Output")

