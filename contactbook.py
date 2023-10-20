import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        update_contact_list()
        clear_entry_fields()
        messagebox.showinfo("Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required fields.")



def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")


def clear_entry_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)



def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        deleted_contact = contacts.pop(index)
        update_contact_list()
        clear_entry_fields()
        messagebox.showinfo("Success", f"Contact '{deleted_contact['Name']}' has been deleted.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")


root = tk.Tk()
root.title("Contact Book")


tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2)

contact_list = tk.Listbox(root)
contact_list.grid(row=5, column=0, columnspan=2)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=6, column=0, columnspan=2)

update_contact_list()

root.mainloop()
