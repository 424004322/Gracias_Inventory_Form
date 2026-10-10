import tkinter as tk
from tkinter import messagebox


class InventoryFormApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Robust Inventory Form")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e1e")

        header_frame = tk.Frame(self.root, bg="#1e3a8a", pady=10)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(header_frame, text="Robust Inventory Form", font=("Arial", 16, "bold"), fg="white", bg="#1e3a8a")
        title_label.pack(anchor="w", padx=15)

        subtitle_label = tk.Label(
            header_frame, text="Computer Shop Inventory Management", font=("Arial", 10), fg="#93c5fd", bg="#1e3a8a")
        subtitle_label.pack(anchor="w", padx=15)

        main_container = tk.Frame(self.root, bg="#1e1e1e", padx=10, pady=10)
        main_container.pack(fill=tk.BOTH, expand=True)

        main_container.columnconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=1)

        left_frame = tk.LabelFrame(main_container, text="Product Information", font=("Arial", 11, "bold"), fg="white",bg="#2d2d2d", padx=15, pady=15)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.name_var = tk.StringVar()
        self.qty_var = tk.StringVar()
        self.price_var = tk.StringVar()

        tk.Label(left_frame, text="Product Name", fg="white", bg="#2d2d2d", font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 2))

        self.name_entry = tk.Entry(left_frame, textvariable=self.name_var, bg="#3c3c3c", fg="white", insertbackground="white")
        self.name_entry.pack(fill=tk.X, pady=(0, 2))

        self.name_val_msg = tk.Label( left_frame, text="Required field", fg="#aaaaaa", bg="#2d2d2d", font=("Arial", 8))
        self.name_val_msg.pack(anchor="w", pady=(0, 10))

        tk.Label(left_frame, text="Quantity", fg="white", bg="#2d2d2d", font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 2))

        self.qty_entry = tk.Entry(left_frame, textvariable=self.qty_var, bg="#3c3c3c", fg="white", insertbackground="white")
        self.qty_entry.pack(fill=tk.X, pady=(0, 2))

        self.qty_val_msg = tk.Label(left_frame, text="Must be a whole number > 0", fg="#aaaaaa", bg="#2d2d2d", font=("Arial", 8))
        self.qty_val_msg.pack(anchor="w", pady=(0, 10))

        tk.Label(left_frame, text="Unit Price (P)", fg="white", bg="#2d2d2d", font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 2))

        self.price_entry = tk.Entry( left_frame, textvariable=self.price_var, bg="#3c3c3c", fg="white", insertbackground="white")
        self.price_entry.pack(fill=tk.X, pady=(0, 2))

        self.price_val_msg = tk.Label( left_frame, text="Must be a valid number > 0", fg="#aaaaaa", bg="#2d2d2d", font=("Arial", 8))
        self.price_val_msg.pack(anchor="w", pady=(0, 15))

        btn_frame = tk.Frame(left_frame, bg="#2d2d2d")
        btn_frame.pack(fill=tk.X, pady=(0, 15))

        self.btn_submit = tk.Button(
            btn_frame,
            text="Submit Product",
            command=self.submit_product,
            bg="#2563eb",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=10,
            pady=5,
        )
        self.btn_submit.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.btn_clear = tk.Button(btn_frame,text="Clear Form",command=self.clear_form,bg="#4b5563",fg="white",font=("Arial", 9),padx=10,pady=5,)
        self.btn_clear.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

        status_frame = tk.LabelFrame(left_frame,text="Validation Messages",font=("Arial", 9, "bold"),fg="white",bg="#2d2d2d",)
        status_frame.pack(fill=tk.X, pady=(5, 0))

        self.overall_status_lbl = tk.Label(status_frame,text="Show current form status here.",fg="#aaaaaa",bg="#2d2d2d",font=("Arial", 9),)
        self.overall_status_lbl.pack(anchor="w", padx=5, pady=5)

        self.name_var.trace_add("write", self.validate_name)
        self.qty_var.trace_add("write", self.validate_quantity)
        self.price_var.trace_add("write", self.validate_price)

        right_frame = tk.Frame(main_container, bg="#1e1e1e")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        out_frame = tk.LabelFrame(right_frame,text="Inventory Output",font=("Arial", 11, "bold"),fg="white",bg="#2d2d2d",padx=10,pady=10,)
        out_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        self.inventory_text = tk.Text(out_frame,height=10,bg="#18181b",fg="#4ade80",font=("Courier", 9),wrap=tk.WORD,)
        self.inventory_text.pack(fill=tk.BOTH, expand=True)

        log_frame = tk.LabelFrame(right_frame,text="Validation Trace Log",font=("Arial", 11, "bold"),fg="white",bg="#2d2d2d",padx=10,pady=10,)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        self.log_text = tk.Text(log_frame,height=8,bg="#18181b",fg="#38bdf8",font=("Courier", 8),wrap=tk.WORD,)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.log_text.insert(tk.END,"Test input | Expected response | Actual response\n" + "-" * 50 + "\n",)

    def validate_name(self, *args):
        val = self.name_var.get().strip()
        if val == "":
            self.name_val_msg.config(
                text="Product name cannot be empty", fg="#f87171"
            )
            self.update_overall_status()
            return False
        else:
            self.name_val_msg.config(text="Valid product name", fg="#4ade80")
            self.update_overall_status()
            return True

    def validate_quantity(self, *args):
        val = self.qty_var.get().strip()
        if val == "":
            self.qty_val_msg.config(
                text="Quantity cannot be empty", fg="#f87171"
            )
            self.update_overall_status()
            return False
        try:
            qty = int(val)
            if qty > 0:
                self.qty_val_msg.config(text="Valid quantity", fg="#4ade80")
                self.update_overall_status()
                return True
            else:
                self.qty_val_msg.config(
                    text="Quantity must be greater than 0", fg="#f87171"
                )
                self.update_overall_status()
                return False
        except ValueError:
            self.qty_val_msg.config(
                text="Quantity must be a whole number", fg="#f87171"
            )
            self.update_overall_status()
            return False

    def validate_price(self, *args):
        val = self.price_var.get().strip()
        if val == "":
            self.price_val_msg.config(
                text="Unit Price cannot be empty", fg="#f87171"
            )
            self.update_overall_status()
            return False
        try:
            price = float(val)
            if price > 0:
                self.price_val_msg.config(text="Valid price", fg="#4ade80")
                self.update_overall_status()
                return True
            else:
                self.price_val_msg.config(
                    text="Unit Price must be greater than 0", fg="#f87171"
                )
                self.update_overall_status()
                return False
        except ValueError:
            self.price_val_msg.config(
                text="Unit Price must be a valid number", fg="#f87171"
            )
            self.update_overall_status()
            return False

    def update_overall_status(self):
        v1 = self.validate_name()
        v2 = self.validate_quantity()
        v3 = self.validate_price()
        if v1 and v2 and v3:
            self.overall_status_lbl.config(
                text="All inputs valid. Ready to submit.", fg="#4ade80"
            )
        else:
            self.overall_status_lbl.config(
                text="Please fix errors above before submitting.", fg="#facc15"
            )

    def submit_product(self):
        name = self.name_var.get().strip()
        qty_str = self.qty_var.get().strip()
        price_str = self.price_var.get().strip()

        if name == "":
            messagebox.showerror(
                "Error", "Please enter a valid product name."
            )
            self.log_trace(f"Name: '{name}'", "Rejected", "Error: Empty name")
            return

        try:
            quantity = int(qty_str)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error", "Quantity must be a positive whole number."
            )
            self.log_trace(
                f"Qty: '{qty_str}'", "Rejected", "Error: Invalid quantity"
            )
            return

        try:
            unit_price = float(price_str)
            if unit_price <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error", "Unit Price must be a positive number."
            )
            self.log_trace(
                f"Price: '{price_str}'", "Rejected", "Error: Invalid price"
            )
            return

        total_value = quantity * unit_price

        record = (
            f"Product Name: {name}\n"
            f"Quantity: {quantity}\n"
            f"Unit Price: P{unit_price:,.2f}\n"
            f"Total Value: P{total_value:,.2f}\n"
            f"Successfully Added\n"
            f"----------------------------------------\n"
        )
        self.inventory_text.insert(tk.END, record)
        self.inventory_text.see(tk.END)

        self.log_trace(
            f"Submit '{name}'", "Product added", "Successfully Added"
        )
        messagebox.showinfo("Success", f"Product '{name}' has been added!")

    def clear_form(self):
        self.name_var.set("")
        self.qty_var.set("")
        self.price_var.set("")

        self.name_val_msg.config(text="Required field", fg="#aaaaaa")
        self.qty_val_msg.config(
            text="Must be a whole number > 0", fg="#aaaaaa"
        )
        self.price_val_msg.config(
            text="Must be a valid number > 0", fg="#aaaaaa"
        )
        self.overall_status_lbl.config(
            text="Form cleared. Show current form status here.", fg="#aaaaaa"
        )

        self.log_trace(
            "Click Clear Form", "Fields reset", "Fields reset successfully"
        )

    def log_trace(self, test_input, expected, actual):
        entry = f"{test_input:<20} | {expected:<18} | {actual}\n"
        self.log_text.insert(tk.END, entry)
        self.log_text.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryFormApp(root)
    root.mainloop()