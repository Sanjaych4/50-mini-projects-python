# Day 36: Manage Contacts (GUI based)
# First GUI based program in this series

import tkinter as tk

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
    
    def get_contacts(self):
        return self.contacts

class ContactGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Manager")

        self.contact_manager = ContactManager()

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(master)
        self.phone_entry.pack()

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.contact_listbox = tk.Listbox(master)
        self.contact_listbox.pack()

        self.update_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.contact_manager.add_contact(name, phone)
        self.update_contacts()

    def update_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_manager.get_contacts():
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

root = tk.Tk()
gui = ContactGUI(root)
root.mainloop()
