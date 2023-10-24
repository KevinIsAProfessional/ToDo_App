#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Git er dun ya lazy shit")

    window_width = 400
    window_height = 200

    # Get screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Find the center point
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Ensure window is not resizable, and starts in windowed mode
    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    main()
