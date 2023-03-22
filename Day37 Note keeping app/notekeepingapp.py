# Day 37: A note-keeping app (GUI Based)
#Another GUI based application

import tkinter as tk

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def get_notes(self):
        return self.notes

class NoteGUI:
    def __init__(self, master):
        self.master = master
        master.title("Note Keeper")

        self.note_manager = NoteManager()

        self.title_label = tk.Label(master, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(master)
        self.title_entry.pack()

        self.content_label = tk.Label(master, text="Content:")
        self.content_label.pack()
        self.content_text = tk.Text(master)
        self.content_text.pack()

        self.add_button = tk.Button(master, text="Add Note", command=self.add_note)
        self.add_button.pack()

        self.note_listbox = tk.Listbox(master)
        self.note_listbox.pack()

        self.update_notes()

    def add_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)
        self.note_manager.add_note(title, content)
        self.update_notes()

    def update_notes(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.note_manager.get_notes():
            self.note_listbox.insert(tk.END, note.title)

        # Write notes to file
        with open("notes.txt", "w") as f:
            for note in self.note_manager.get_notes():
                f.write(f"{note.title}\n{note.content}\n")

root = tk.Tk()
gui = NoteGUI(root)
root.mainloop()
