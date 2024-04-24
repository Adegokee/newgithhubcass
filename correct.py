from tkinter import *
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect("user_credentials.db")  # Fix the database name here
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_credentials():
    email = email_entry.get()
    password = password_entry.get()

    if email and password:
        conn = sqlite3.connect("user_credentials.db")  # Fix the database name here
        cursor = conn.cursor()
        cursor.execute("INSERT INTO credentials (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Credentials successfully created")
    else:
        messagebox.showwarning("Error", "Error creating Credentials")

def display_credentials():
    conn = sqlite3.connect("user_credentials.db")  # Fix the database name here
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credentials")
    data = cursor.fetchall()
    conn.close()

    if data:
        result_text.delete(1.0, END)
        for entry in data:
            result_text.insert(END, f'Email: {entry[1]}\nPassword: {entry[2]}\n\n')
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "No data found")

window = Tk()
window.title("Email and Password Management")
create_table()

email_label = Label(window, text="Email")
email_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
email_entry = Entry(window)
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(window, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
password_entry = Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

save_button = Button(window, text="Save Credentials", command=save_credentials)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

display_button = Button(window, text="Display Credentials", command=display_credentials)
display_button.grid(row=3, column=0, columnspan=2, pady=10)

result_text = Text(window, height=10, width=40)
result_text.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()