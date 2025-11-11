import os
import sys
import tkinter as tk

# Tambahkan direktori root ke path Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    app = MainWindow(root)
    app.run()

if __name__ == "__main__":
    main()
