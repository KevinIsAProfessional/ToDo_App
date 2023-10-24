#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk


def add_tree(parent_frame):
    # Use TreeView to display all todo items
    columns = ('status', 'task')

    # FIXME: change 'tree headings' to 'headings'
    tree = ttk.Treeview(parent_frame, columns=columns, show='headings')

    tree.heading('status', text='Status')
    tree.heading('task', text='Task description')

    # Set geometry and add to parent frame
    tree.column('status', width=80, anchor=tk.W)
    tree.column('task', width=320, anchor=tk.E)
    tree.grid(row=0, column=0, sticky='nsew')


def add_input(parent_frame):
    # FIXME: width and height are hardcoded - change to dynamic later
    input_form = tk.Frame(parent_frame, height=100, width=400)

    placeholder = tk.Label(input_form, text="New ToDo")
    placeholder.grid(row=0, column=0, sticky='w')

    input_field = tk.Entry(input_form)
    input_field.grid(row=0, column=2, sticky='w')

    input_button = tk.Button(input_form, text='accept')
    input_button.grid(row=0, column=2, sticky='e')

    input_form.grid(row=1, column=0, sticky='s')


def main():
    root = tk.Tk()
    root.title("Git er dun ya lazy shit")

    window_width = 400
    window_height = 255

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

    # add the task list to the frame
    add_tree(root)

    # Add the task adding form to the frame
    add_input(root)

    root.mainloop()


if __name__ == "__main__":
    main()
