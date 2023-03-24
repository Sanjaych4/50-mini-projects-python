# Day 47: Wallpaper loop

import os
import time
import ctypes

def change_wallpaper(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(os.path.join(folder_path, filename))

    while True:
        for image in images:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
            time.sleep(1800)

if __name__ == '__main__':
    folder_path = r'C:\Users\Username\Pictures\Wallpapers'  #replace with your folder path
    change_wallpaper(folder_path)
