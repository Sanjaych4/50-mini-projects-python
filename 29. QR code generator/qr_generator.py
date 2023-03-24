# Day 29: QR Code generator

# `pip install qrcode` install this in the terminal before running the program
import os
import qrcode
from PIL import Image

# Take Input from User
input_data = input("Enter the data you want to encode in QR Code: ")

# Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)

# Create Image
img = qr.make_image(fill_color="black", back_color="white")

# Get Current Directory and Save Image
dir_path = os.path.dirname(os.path.realpath(__file__))
img.save(os.path.join(dir_path, "qrcode.png"))

# Display Image (Optional)
img.show()
