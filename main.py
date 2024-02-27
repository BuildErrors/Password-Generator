import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Analytical AI Password Generator")
        self.master.configure(bg="#f0f0f0")

        self.banner_color = "#64fab4"
        self.label_title = tk.Label(master, text="Analytical AI Password Generator", font=("Helvetica", 25), bg=self.banner_color, fg="white")
        self.label_title.pack(fill=tk.X, pady=50, padx = 150)

        self.password_var = tk.StringVar()
        self.password_var.set("")

        self.password_frame = tk.Frame(master, bd=2, relief=tk.SOLID, bg="#f0f0f0")
        self.password_frame.pack(pady=10, padx=20)

        self.label_password = tk.Label(self.password_frame, textvariable=self.password_var, font=("Helvetica", 14), bg="#f0f0f0")
        self.label_password.pack(pady=5, padx=10)

        self.button_style = ttk.Style()
        self.button_style.configure('TButton', font=('Helvetica', 12, 'bold'), background='black', foreground='gray', borderwidth=0, relief=tk.FLAT)
        self.button_generate = ttk.Button(master, text="Generate Password", command=self.generate_password, style='TButton')
        self.button_generate.pack(pady=10, padx=20, ipadx=10, ipady=15, fill=tk.X)

        self.button_copy = ttk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, style='TButton')
        self.button_copy.pack(pady=5, padx=20, ipadx=10, ipady=15, fill=tk.X)

        self.button_save = ttk.Button(master, text="Save to File", command=self.save_to_file, style='TButton')
        self.button_save.pack(pady=5, padx=20, ipadx=10, ipady=15, fill=tk.X)

        # Allow widgets to expand/resize with window
        master.pack_propagate(False)

    def generate_password(self):
        length = 12
        complexity = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(complexity) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Password Generator", "Password copied to clipboard!")

    def save_to_file(self):
        password = self.password_var.get()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(password)
            messagebox.showinfo("Password Generator", f"Password saved to {file_path}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
