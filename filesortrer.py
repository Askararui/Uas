import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkfont

def sort_files():
    # Change button state and appearance while processing
    button.config(state='disabled', bg='#8fa3f5')
    root.update()
    
    folder_path = filedialog.askdirectory(title="Pilih Folder yang Ingin Disortir")
    if not folder_path:
        button.config(state='normal', bg=BUTTON_COLOR)
        return

    # 🔹 Popup untuk memilih tindakan setelah folder dipilih
    action_window = tk.Toplevel(root)
    action_window.title("Pilih Tindakan")
    action_window.geometry("300x180")
    action_window.configure(bg=BG_COLOR)
    action_window.resizable(False, False)

    tk.Label(action_window, text="Apa yang ingin Anda lakukan dengan file?", 
             font=custom_font, bg=BG_COLOR, fg=TEXT_COLOR, wraplength=250, justify="center").pack(pady=(15, 10))

    action_choice = tk.StringVar(value="move")

    tk.Radiobutton(action_window, text="Pindahkan file (hapus dari lokasi asal)", 
                   variable=action_choice, value="move", bg=BG_COLOR, fg=TEXT_COLOR, font=custom_font).pack(anchor='w', padx=25)
    tk.Radiobutton(action_window, text="Salin file (tetap di lokasi asal)", 
                   variable=action_choice, value="copy", bg=BG_COLOR, fg=TEXT_COLOR, font=custom_font).pack(anchor='w', padx=25)

    def start_sort():
        action = action_choice.get()
        action_window.destroy()  # Tutup popup sebelum mulai sortir

        folders = {
            '📷 Gambar': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
            '📄 Dokumen': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.xls', '.ppt'],
            '🎥 Video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
            '🎵 Musik': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg'],
            '📦 Arsip': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            '📁 Lainnya': []
        }

        for folder in folders:
            path = os.path.join(folder_path, folder)
            if not os.path.exists(path):
                os.makedirs(path)

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        total_files = len(files)
        if total_files == 0:
            messagebox.showinfo("Info", "Tidak ada file di folder ini.")
            button.config(state='normal', bg=BUTTON_COLOR)
            return

        moved_count = 0

        # 🔹 Simulasi loading kecil sebelum mulai
        root.update()
        messagebox.showinfo("Proses Dimulai", "Menyortir file, harap tunggu...")

        for i, file_name in enumerate(files, start=1):
            file_path = os.path.join(folder_path, file_name)
            _, ext = os.path.splitext(file_name)
            moved = False

            for folder, extensions in folders.items():
                if ext.lower() in extensions:
                    dest = os.path.join(folder_path, folder, file_name)
                    if action == "move":
                        shutil.move(file_path, dest)
                    else:
                        shutil.copy2(file_path, dest)
                    moved = True
                    break

            if not moved:
                dest = os.path.join(folder_path, '📁 Lainnya', file_name)
                if action == "move":
                    shutil.move(file_path, dest)
                else:
                    shutil.copy2(file_path, dest)

            moved_count += 1

        messagebox.showinfo("Selesai", f"{moved_count} file telah disortir ke dalam folder sesuai jenisnya.")
        button.config(state='normal', bg=BUTTON_COLOR)

    tk.Button(action_window, text="Mulai", command=start_sort,
              bg=BUTTON_COLOR, fg="white", font=custom_font, bd=0, padx=20, pady=5,
              activebackground="#3a5bd9", activeforeground="white", cursor="hand2").pack(pady=15)

# ================= GUI utama =================
BG_COLOR = "#f0f2f5"
BUTTON_COLOR = "#4a6cf7"
TEXT_COLOR = "#333333"
FRAME_COLOR = "#ffffff"

# Configure root window
root = tk.Tk()
root.title("File Sorter")
root.geometry("400x320")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Custom font
custom_font = tkfont.Font(family="Segoe UI", size=10)
header_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")

# Main container
main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

# Header
header_frame = tk.Frame(main_frame, bg=BG_COLOR)
header_frame.pack(pady=(0, 15))

# App icon/logo (using emoji as icon)
icon_label = tk.Label(header_frame, text="📁", font=("Segoe UI", 32), bg=BG_COLOR)
icon_label.pack(side=tk.LEFT, padx=(0, 15))

# Title and subtitle
title_frame = tk.Frame(header_frame, bg=BG_COLOR)
title_frame.pack(side=tk.LEFT)
tk.Label(title_frame, text="File Sorter", font=header_font, bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor='w')
tk.Label(title_frame, text="Atur file Anda dengan mudah", font=custom_font, bg=BG_COLOR, fg="#666666").pack(anchor='w')

# Content frame
content_frame = tk.Frame(main_frame, bg=BG_COLOR)
content_frame.pack(expand=True, fill='both', pady=10)

# Instructions
tk.Label(content_frame, 
         text="Pilih folder yang berisi file-file yang ingin Anda sortir.",
         font=custom_font,
         bg=BG_COLOR,
         fg=TEXT_COLOR,
         wraplength=300,
         justify=tk.CENTER).pack(pady=(0, 10))

# Sort button
button = tk.Button(content_frame, 
                  text="📂  Pilih Folder & Mulai Sortir", 
                  command=sort_files,
                  bg=BUTTON_COLOR,
                  fg="white",
                  font=custom_font,
                  bd=0,
                  padx=20,
                  pady=8,
                  activebackground="#3a5bd9",
                  activeforeground="white",
                  cursor="hand2")
button.pack(pady=(0, 15), ipadx=10, ipady=2)

# 🔹 Tambahan menu About
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Tentang Aplikasi")
    about_window.geometry("350x250")
    about_window.configure(bg=BG_COLOR)
    about_window.resizable(False, False)

    tk.Label(about_window, text="📦 Tentang File Sorter", font=header_font, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(15, 5))
    tk.Label(about_window, 
             text="Aplikasi ini membantu Anda menyortir file berdasarkan jenisnya "
                  "secara otomatis ke dalam folder seperti Gambar, Dokumen, Video, Musik, dan lainnya.",
             font=custom_font, bg=BG_COLOR, fg=TEXT_COLOR, wraplength=300, justify="center").pack(pady=(10, 10))
    tk.Label(about_window, 
             text="Dibuat dengan sungguh-sungguh menggunakan Python & Tkinter\noleh Kelompok \nCemani Kulit Hitam Pekat.",
             font=("Segoe UI", 9), bg=BG_COLOR, fg="#555555", justify="center").pack(pady=(10, 5))

    tk.Button(about_window, text="Tutup", command=about_window.destroy,
              bg=BUTTON_COLOR, fg="white", font=custom_font, bd=0, padx=15, pady=5,
              activebackground="#3a5bd9", activeforeground="white", cursor="hand2").pack(pady=10)

menubar = tk.Menu(root)
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="Tentang Aplikasi", command=show_about)
menubar.add_cascade(label="Bantuan", menu=about_menu)
root.config(menu=menubar)

# Sedikit perataan biar layout tetap rapi meski ada menu bar
main_frame.pack_configure(pady=(10, 20))

root.mainloop()
