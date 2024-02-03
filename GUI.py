import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to initialize database
def initialize_database():
    conn = sqlite3.connect('crud_app.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to create a new user
def create_user():
    name = name_entry.get()
    email = email_entry.get()

    conn = sqlite3.connect('crud_app.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "User created successfully!")

# Function to read users from the database
def read_users():
    conn = sqlite3.connect('crud_app.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    user_listbox.delete(0, tk.END)
    for user in users:
        user_listbox.insert(tk.END, user)

    conn.close()

# Function to delete selected user
def delete_user():
    selected_user = user_listbox.get(tk.ACTIVE)
    user_id = selected_user[0]

    conn = sqlite3.connect('crud_app.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "User deleted successfully!")

# Create the main window
root = tk.Tk()
root.title("CRUD Application")

# Create and pack labels and entry fields for name and email
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Create and pack buttons for CRUD operations
create_button = tk.Button(root, text="Create", command=create_user)
create_button.grid(row=2, column=0, padx=5, pady=5)

read_button = tk.Button(root, text="Read", command=read_users)
read_button.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_user)
delete_button.grid(row=2, column=2, padx=5, pady=5)

# Create and pack listbox to display users
user_listbox = tk.Listbox(root, width=50)
user_listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Initialize database
initialize_database()

# Start the Tkinter event loop
root.mainloop()
