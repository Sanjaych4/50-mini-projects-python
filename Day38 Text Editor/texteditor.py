# Day 38: A simple text editor (GUI Based)

import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("500x500")
        
        # create a menu bar
        menubar = tk.Menu(self.master)
        
        # create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # create an edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        # create a view menu
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.zoom_out)
        menubar.add_cascade(label="View", menu=view_menu)
        
        # set the menu bar
        self.master.config(menu=menubar)
        
        # create a text widget
        self.text = tk.Text(self.master)
        self.text.pack(expand=True, fill="both")
    
    def new_file(self):
        self.text.delete(1.0, tk.END)
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, text)
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                text = self.text.get(1.0, tk.END)
                file.write(text)
    
    def cut(self):
        self.text.event_generate("<<Cut>>")
    
    def copy(self):
        self.text.event_generate("<<Copy>>")
    
    def paste(self):
        self.text.event_generate("<<Paste>>")
    
    def zoom_in(self):
        font_size = self.text.cget("font").split(" ")[-1]
        new_size = int(font_size) + 2
        self.text.configure(font=("TkDefaultFont", new_size))
    
    def zoom_out(self):
        font_size = self.text.cget("font").split(" ")[-1]
        new_size = int(font_size) - 2
        if new_size > 0:
            self.text.configure(font=("TkDefaultFont", new_size))

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()

