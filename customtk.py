import tkinter as tk

class CustomLabeledEntry(tk.Frame):
    def __init__(self, master=None, label_text="Label", **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text=label_text)
        self.label.grid(row=0, column=0, padx=(0, 5))
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1)


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Labeled Entry Widget")
    custom_entry_widget = CustomLabeledEntry(root, label_text="Name:")
    custom_entry_widget.pack(padx=10, pady=10)
    root.mainloop()


# import tkinter as tk
# from tkinter import scrolledtext

# class CustomCodeWidget(scrolledtext.ScrolledText):
#     def __init__(self, master=None, **kwargs):
#         super().__init__(master, **kwargs)
#         self.configure(font=("Courier New", 12), wrap=tk.WORD)

# # Example usage:
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Custom Code Widget")

#     custom_code_widget = CustomCodeWidget(root, width=40, height=10)
#     custom_code_widget.pack(padx=10, pady=10)

#     code_example = """def hello_world():
#     print("Hello, World!")

# hello_world()
# """
#     custom_code_widget.insert(tk.END, code_example)




#     root.mainloop()

# import tkinter as tk

# class CustomButton(tk.Button):
#     def __init__(self, master=None, **kwargs):
#         tk.Button.__init__(self, master, **kwargs)
#         self.bind("<Enter>", self.on_enter)
#         self.bind("<Leave>", self.on_leave)

#     def on_enter(self, event):
#         self.config(bg='lightgray')

#     def on_leave(self, event):
#         self.config(bg='white')

# root = tk.Tk()

# custom_button = CustomButton(root, text="Hover me")
# custom_button.pack()

# root.mainloop()
