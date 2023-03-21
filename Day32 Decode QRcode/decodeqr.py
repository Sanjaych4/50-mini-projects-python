# Day 32: Decode a QR Code
# `pip install pyzbar` and `pip install opencv-python` install pyzbar module before running this program

import cv2
from pyzbar import pyzbar

# Load the image containing the QR code
image = cv2.imread("qr_code.png")

# Decode the QR code using pyzbar
barcodes = pyzbar.decode(image)

# Loop through all the detected barcodes
for barcode in barcodes:
    # Print the data and barcode type
    print("Data:", barcode.data.decode("utf-8"))
    print("Type:", barcode.type)
    
    # Draw a bounding box around the barcode on the image
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image with the detected barcodes and bounding boxes
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
