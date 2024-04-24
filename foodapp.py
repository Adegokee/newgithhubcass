import tkinter as tk
from tkinter import messagebox
import sqlite3

class FoodOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Ordering App")

        # Initialize the database
        self.conn = sqlite3.connect('food_ordering.db')
        self.create_table()

        # GUI elements
        self.menu_label = tk.Label(root, text="Menu:")
        self.menu_label.pack()

        self.menu_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.menu_listbox.pack()

        self.order_button = tk.Button(root, text="Place Order", command=self.place_order)
        self.order_button.pack()

        # Populate menu items
        self.populate_menu()

    def create_table(self):
        # Create a table to store menu items
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS menu
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           item TEXT NOT NULL,
                           price REAL NOT NULL)''')
        self.conn.commit()

    def populate_menu(self):
        # Add some sample menu items
        menu_items = [('Pizza', 10.99), ('Burger', 5.99), ('Salad', 7.99)]
        cursor = self.conn.cursor()
        cursor.executemany('INSERT INTO menu (item, price) VALUES (?, ?)', menu_items)
        self.conn.commit()

        # Display menu items in the listbox
        for item in cursor.execute('SELECT item FROM menu'):
            self.menu_listbox.insert(tk.END, item[0])

    def place_order(self):
        # Get selected menu items
        selected_items = [self.menu_listbox.get(i) for i in self.menu_listbox.curselection()]

        if not selected_items:
            messagebox.showinfo("Order Confirmation", "Please select at least one item.")
            return

        total_price = 0.0
        cursor = self.conn.cursor()

        # Calculate total price
        for item in selected_items:
            cursor.execute('SELECT price FROM menu WHERE item=?', (item,))
            total_price += cursor.fetchone()[0]

        # Show order confirmation
        messagebox.showinfo("Order Confirmation", f"Order placed!\nItems: {', '.join(selected_items)}\nTotal Price: ${total_price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderingApp(root)
    root.mainloop()
