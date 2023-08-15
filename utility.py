from tkinter import *
from tkinter import ttk


def set_grid(obj, row, col, columnspan=None):
    return obj.grid(row=row, column=col, padx=10, pady=10, columnspan=columnspan)


def create_button(window, text, row, column, command, columnspan=None):
    button = Button(window, text=text, command=command)
    set_grid(button, row, column, columnspan)
    return button


def create_entry(window, row, column, columnspan=None):
    entry = Entry(window)
    set_grid(entry, row, column, columnspan)
    return entry


def create_label(win, text, row, column, columnspan=None):
    label = Label(win, text=text)
    set_grid(label, row, column, columnspan)
    return label


def create_treeview(win, columns, widths, headings):
    treeview = ttk.Treeview(win, columns=columns)

    treeview.column("#0", anchor=CENTER, width=50)
    treeview.heading("#0", text="ID")
    for index, column in enumerate(columns):
        treeview.column(column, anchor=CENTER, width=widths[index])
        treeview.heading(column, text=headings[index])
    treeview.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=NSEW)
    return treeview
