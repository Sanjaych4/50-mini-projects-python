# Day 38: A simple text editor (GUI Based)

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:

    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")

        self.textarea = tk.Text(self.master, wrap=tk.WORD)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.textarea.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textarea.configure(yscrollcommand=self.scrollbar.set)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menubar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command(label="Zoom In", command=self.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.zoom_out)
        menubar.add_cascade(label="View", menu=view_menu)

        mode_menu = tk.Menu(menubar, tearoff=False)
        mode_menu.add_command(label="Light Mode", command=self.light_mode)
        mode_menu.add_command(label="Dark Mode", command=self.dark_mode)
        menubar.add_cascade(label="Mode", menu=mode_menu)

    def new_file(self):
        self.textarea.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, text)

    def save_file(self):
        try:
            file = open(self.file_path, "w")
            text = self.textarea.get("1.0", tk.END)
            file.write(text)
            file.close()
        except AttributeError:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            self.file_path = file_path
            self.save_file()

    def zoom_in(self):
        font_size = int(self.textarea["font"].split()[1])
        font_size += 2
        self.textarea.configure(font=("TkDefaultFont", font_size))

    def zoom_out(self):
        font_size = int(self.textarea["font"].split()[1])
        font_size -= 2
        if font_size > 0:
            self.textarea.configure(font=("TkDefaultFont", font_size))

    def light_mode(self):
        self.master.configure(bg="white")
        self.textarea.configure(bg="white", fg="black")

    def dark_mode(self):
        self.master.configure(bg="black")
        self.textarea.configure(bg="black", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


