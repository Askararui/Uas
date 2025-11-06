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
        return

    progress_bar["maximum"] = total_files
    moved_count = 0

    for i, file_name in enumerate(files, start=1):
        file_path = os.path.join(folder_path, file_name)
        _, ext = os.path.splitext(file_name)
        moved = False

        for folder, extensions in folders.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file_name))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, 'Lainnya', file_name))

        moved_count += 1
        progress_bar["value"] = i
        root.update_idletasks()

    messagebox.showinfo("Selesai", f"{moved_count} file telah disortir ke dalam folder sesuai jenisnya.")
    progress_bar["value"] = 0  # Reset setelah selesai
    button.config(state='normal', bg=BUTTON_COLOR)  # Re-enable button

# GUI utama
# Configure colors
BG_COLOR = "#f0f2f5"
BUTTON_COLOR = "#4a6cf7"
TEXT_COLOR = "#333333"
FRAME_COLOR = "#ffffff"

# Configure root window
root = tk.Tk()
root.title("File Sorter")
root.geometry("400x250")
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
         justify=tk.CENTER).pack(pady=(0, 20))

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

# Progress bar frame
progress_frame = tk.Frame(content_frame, bg=BG_COLOR)
progress_frame.pack(fill='x', pady=5)

# Progress bar with label
progress_label = tk.Label(progress_frame, 
                         text="Progres:", 
                         font=custom_font, 
                         bg=BG_COLOR,
                         fg=TEXT_COLOR)
progress_label.pack(anchor='w')

style = ttk.Style()
style.configure("Custom.Horizontal.TProgressbar",
                troughcolor ="#e0e0e0",
                background =BUTTON_COLOR,
                bordercolor ="#e0e0e0",
                lightcolor =BUTTON_COLOR,
                darkcolor =BUTTON_COLOR)

progress_bar = ttk.Progressbar(progress_frame, 
                             orient="horizontal", 
                             length=300, 
                             mode="determinate",
                             style="Custom.Horizontal.TProgressbar")
progress_bar.pack(fill='x', pady=(5, 0))

root.mainloop()
