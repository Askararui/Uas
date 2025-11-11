import tkinter as tk
from tkinter import ttk

class AboutWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Tentang Aplikasi")
        self.window.geometry("350x250")
        self.window.configure(bg="#f0f2f5")
        self.window.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        # Header
        header_font = ("Segoe UI", 12, "bold")
        tk.Label(
            self.window, 
            text="📦 Tentang File Sorter", 
            font=header_font, 
            bg="#f0f2f5", 
            fg="#333333"
        ).pack(pady=(15, 5))

        # Description
        description = (
            "Aplikasi ini membantu Anda menyortir file berdasarkan jenisnya "
            "secara otomatis ke dalam folder seperti Gambar, Dokumen, Video, "
            "Musik, dan lainnya."
        )
        
        tk.Label(
            self.window,
            text=description,
            font=("Segoe UI", 9),
            bg="#f0f2f5",
            fg="#333333",
            wraplength=300,
            justify="center"
        ).pack(pady=(10, 10))

        # Credits
        tk.Label(
            self.window,
            text=(
                "Dibuat dengan sungguh-sungguh menggunakan Python & Tkinter\n"
                "oleh Kelompok \nCemani Kulit Hitam Pekat."
            ),
            font=("Segoe UI", 9),
            bg="#f0f2f5",
            fg="#555555",
            justify="center"
        ).pack(pady=(10, 5))

        # Close button
        close_btn = ttk.Button(
            self.window,
            text="Tutup",
            command=self.window.destroy,
            style="Accent.TButton"
        )
        close_btn.pack(pady=10)

    def show(self):
        self.window.grab_set()
        self.window.wait_window()
