import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Labels and Entry fields for name, phone, email, and address
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for adding, viewing, updating, searching, and deleting contacts
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.view_button = tk.Button(root, text="View Contact", command=self.view_contact)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, width=50)
        self.contact_listbox.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        # Get contact information from entry fields
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Check if all fields are filled
        if name and phone and email and address:
            # Create contact string
            contact_info = f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}"

            # Append contact to contacts list
            self.contacts.append(contact_info)

            # Insert contact into listbox
            self.contact_listbox.insert(tk.END, contact_info)

            # Clear entry fields
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def view_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact_info = self.contacts[index]
            messagebox.showinfo("Contact Information", contact_info)
        else:
            messagebox.showerror("Error", "Please select a contact to view.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]

            # Get current contact information
            old_contact_info = self.contacts[index]

            # Get updated contact information from entry fields
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            # Check if all fields are filled
            if name and phone and email and address:
                # Create updated contact string
                updated_contact_info = f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}"

                # Update contact in contacts list
                self.contacts[index] = updated_contact_info

                # Update contact in listbox
                self.contact_listbox.delete(index)
                self.contact_listbox.insert(index, updated_contact_info)

                # Clear entry fields
                self.clear_entry_fields()
            else:
                messagebox.showerror("Error", "Please fill all fields.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def search_contact(self):
        search_term = self.name_entry.get().lower()
        if search_term:
            search_results = []
            for contact in self.contacts:
                if search_term in contact.lower():
                    search_results.append(contact)
            self.contact_listbox.delete(0, tk.END)
            for result in search_results:
                self.contact_listbox.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.contact_listbox.delete(index)
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
