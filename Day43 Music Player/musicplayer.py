# Day 43: A music player
# `pip install pygame`` before running this program

import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x150")
        self.current_song = None
        self.initialize_ui()

    def initialize_ui(self):
        # create the UI elements
        self.song_label = tk.Label(self.root, text="No song selected")
        self.song_label.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.open_button = tk.Button(self.root, text="Open", command=self.open_music_file)
        self.open_button.pack(side=tk.LEFT, padx=10)

    def play_music(self):
        if self.current_song:
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def open_music_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.current_song = file_path
            pygame.mixer.music.load(file_path)
            self.song_label.config(text=os.path.basename(file_path))

if __name__ == "__main__":
    pygame.init()
    root = tk.Tk()
    MusicPlayer(root)
    root.mainloop()
