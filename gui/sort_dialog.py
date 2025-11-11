import tkinter as tk
from tkinter import ttk

class SortDialog:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.action = "move"
        
        self.window = tk.Toplevel(parent)
        self.window.title("Pilih Tindakan")
        self.window.geometry("300x180")
        self.window.configure(bg="#f0f2f5")
        self.window.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        tk.Label(
            self.window,
            text="Apa yang ingin Anda lakukan dengan file?",
            font=("Segoe UI", 10),
            bg="#f0f2f5",
            fg="#333333",
            wraplength=250,
            justify="center"
        ).pack(pady=(15, 10))
        
        # Radio buttons
        self.action_var = tk.StringVar(value="move")
        
        ttk.Radiobutton(
            self.window,
            text="Pindahkan file (hapus dari lokasi asal)",
            variable=self.action_var,
            value="move"
        ).pack(anchor='w', padx=25, pady=2)
        
        ttk.Radiobutton(
            self.window,
            text="Salin file (tetap di lokasi asal)",
            variable=self.action_var,
            value="copy"
        ).pack(anchor='w', padx=25, pady=2)
        
        # Start button
        start_btn = ttk.Button(
            self.window,
            text="Mulai",
            command=self.on_start,
            style="Accent.TButton"
        )
        start_btn.pack(pady=15)
    
    def on_start(self):
        self.action = self.action_var.get()
        self.callback(self.action)
        self.window.destroy()
    
    def show(self):
        self.window.grab_set()
        self.window.wait_window()
        return self.action
