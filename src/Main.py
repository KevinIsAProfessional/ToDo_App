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
    tree.column('task', width=320, anchor=tk.W)
    tree.grid(row=0, column=0, sticky='nsew')

    return tree


def add_input(parent_frame, tree_frame):
    """ Adds a frame to the bottom of the window which accepts user
        input to add new tasks to the Treeview frame"""

    # FIXME: width and height are hardcoded - change to dynamic later
    # height=100, width=600)
    input_form = tk.Frame(parent_frame)

    placeholder = tk.Label(input_form, text="New task")
    placeholder.grid(row=0, column=0)

    # Add entry field for task text
    input_field = tk.Entry(input_form)
    input_field.grid(row=0, column=1)

    # Add dropdown selection for task type
    task_types = ["TODO", "DONE", "URGE"]
    input_type = ttk.Combobox(input_form, values=task_types)
    input_type.set("Task type")
    input_type.grid(row=0, column=2)

    # Add button to accept new tasks and add them to the Treeview
    def on_press(): return add_task(tree_frame, input_field, input_type)
    input_accept = tk.Button(input_form, text='accept', command=on_press)
    input_accept.grid(row=0, column=3)

    input_form.grid(row=1, column=0, sticky='nsew')


def add_task(tree_frame, input_field, input_type):
    task_type = input_type.get()
    task_text = input_field.get()
    task = (task_type, task_text)
    tree_frame.insert('', tk.END, values=task)


def main():
    root = tk.Tk()
    root.title("Git er dun ya lazy shit")

    window_width = 520
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
    tree = add_tree(root)

    # Add the task adding form to the frame
    add_input(root, tree)

    root.mainloop()


if __name__ == "__main__":
    main()
