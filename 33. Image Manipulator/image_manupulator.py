# Day 33: An image manipulator (contrast, brightness, etc.)
# `pip install opencv-python` install opencv module before running this program
import cv2

# Load the image
image = cv2.imread("image.jpg")

# Adjust the contrast and brightness
contrast = 1.5
brightness = 25
adjusted_image = cv2.addWeighted(image, contrast, image, 0, brightness)

# Display the original and adjusted images side by side
cv2.imshow("Original Image", image)
cv2.imshow("Adjusted Image", adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
