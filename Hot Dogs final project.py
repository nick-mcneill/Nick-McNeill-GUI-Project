""" Final Project: Create a GUI
    My GUI program will be an ordering system for a hot dog stand, it will have two windows,
    the first of which the user will be prompted to choose a size of hotdog. The next
    window will then display, asking the user to input which condiments he or she
    would like on their hotdog.
    Nick McNeill 9/30/24
"""
import tkinter as tk
from tkinter import messagebox

class HotDogOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hot Dog Ordering System")
        self.root.geometry("600x400")
        self.root.configure(bg="light blue")

        self.size_price = {"Regular": 5.00, "Large": 7.00}
        self.condiment_price = {"Ketchup": 0.50, "Mustard": 0.50, "Relish": 0.75, "Onions": 0.75, "Jalapeno": 0.75}
        self.selected_size = tk.StringVar()
        self.selected_condiments = []

        self.create_size_selection_window()

    def create_size_selection_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Choose Hot Dog Size", bg="light blue", font=("Arial", 20)).pack(pady=20)

        for size in self.size_price.keys():
            tk.Radiobutton(self.root, text=size, variable=self.selected_size, value=size, bg="light blue", font=("Arial", 16)).pack(anchor=tk.W, padx=20)

        tk.Button(self.root, text="Next", command=self.create_condiment_selection_window, font=("Arial", 16)).pack(pady=20)

    def create_condiment_selection_window(self):
        if not self.selected_size.get():
            messagebox.showwarning("Selection Error", "Please select a hot dog size.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Choose Condiments", bg="light blue", font=("Arial", 20)).pack(pady=20)

        self.condiment_vars = {}
        for condiment in self.condiment_price.keys():
            var = tk.BooleanVar()
            self.condiment_vars[condiment] = var
            tk.Checkbutton(self.root, text=condiment, variable=var, bg="light blue", font=("Arial", 16)).pack(anchor=tk.W, padx=20)

        tk.Button(self.root, text="Calculate Price", command=self.calculate_price, font=("Arial", 16)).pack(pady=20)

    def calculate_price(self):
        total_price = self.size_price[self.selected_size.get()]
        for condiment, var in self.condiment_vars.items():
            if var.get():
                total_price += self.condiment_price[condiment]

        messagebox.showinfo("Order Summary", f"Total Price: ${total_price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotDogOrderApp(root)
    root.mainloop()

