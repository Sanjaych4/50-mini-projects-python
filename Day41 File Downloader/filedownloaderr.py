# Day 41: File Downloader

import requests
url = input("Enter URL: ")
filename = input("Enter filename: ")
response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)
print("Downloaded", filename)
