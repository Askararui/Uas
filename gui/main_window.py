import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkfont
from .about_window import AboutWindow
from utils.file_operations import sort_files

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.setup_menu()
    
    def setup_window(self):
        self.root.title("File Sorter")
        self.root.geometry("400x320")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(False, False)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("Accent.TButton",
                           background="#4a6cf7",
                           foreground="white",
                           font=("Segoe UI", 10))
        self.style.map('Accent.TButton',
                     foreground=[('active', 'white'), ('!disabled', 'white')],
                     background=[('active', '#3a5bd9'), ('!disabled', '#4a6cf7')])
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("Accent.TButton", 
                           background="#4a6cf7",
                           foreground="white",
                           font=("Segoe UI", 10))
        
        # Custom fonts
        self.custom_font = tkfont.Font(family="Segoe UI", size=10)
        self.header_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")
    
    def create_widgets(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(expand=True, fill='both')
        
        # Header
        self.create_header()
        
        # Content
        self.create_content()
    
    def create_header(self):
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(pady=(0, 15))
        
        # App icon/logo
        icon_label = ttk.Label(header_frame, text="📁", font=("Segoe UI", 32))
        icon_label.pack(side=tk.LEFT, padx=(0, 15))
        
        # Title and subtitle
        title_frame = ttk.Frame(header_frame)
        title_frame.pack(side=tk.LEFT)
        
        ttk.Label(
            title_frame,
            text="File Sorter",
            font=self.header_font,
            foreground="#333333"
        ).pack(anchor='w')
        
        ttk.Label(
            title_frame,
            text="Atur file Anda dengan mudah",
            font=self.custom_font,
            foreground="#666666"
        ).pack(anchor='w')
    
    def create_content(self):
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(expand=True, fill='both', pady=10)
        
        # Instructions
        ttk.Label(
            content_frame,
            text="Pilih folder yang berisi file-file yang ingin Anda sortir.",
            font=self.custom_font,
            foreground="#333333",
            wraplength=300,
            justify=tk.CENTER
        ).pack(pady=(0, 10))
        
        # Sort button
        self.sort_btn = ttk.Button(
            content_frame,
            text="📂  Pilih Folder & Mulai Sortir",
            command=self.on_sort_click,
            style="Accent.TButton",
            padding=(20, 8)
        )
        self.sort_btn.pack(pady=(0, 15), ipadx=10, ipady=2)
    
    def setup_menu(self):
        menubar = tk.Menu(self.root)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tentang Aplikasi", command=self.show_about)
        menubar.add_cascade(label="Bantuan", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def on_sort_click(self):
        folder_path = filedialog.askdirectory(title="Pilih Folder yang Ingin Disortir")
        if not folder_path:
            return
        
        # Show sort options dialog
        from .sort_dialog import SortDialog
        
        def start_sorting(action):
            self.sort_btn.config(state='disabled')
            self.root.update()
            
            try:
                files_processed = sort_files(folder_path, action)
                if files_processed > 0:
                    messagebox.showinfo(
                        "Selesai",
                        f"{files_processed} file telah disortir ke dalam folder sesuai jenisnya."
                    )
                else:
                    messagebox.showinfo("Info", "Tidak ada file yang perlu disortir di folder ini.")
            except Exception as e:
                messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            finally:
                self.sort_btn.config(state='normal')
        
        SortDialog(self.root, start_sorting)
    
    def show_about(self):
        about_window = AboutWindow(self.root)
        about_window.show()
    
    def run(self):
        self.root.mainloop()
