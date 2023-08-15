from utility import *
from databaze import *
from tkinter import messagebox


class ViewByCapacityWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Просмотреть грузовой транспорт по грузоподъемности")
        self.geometry("600x300")

        self.create_widgets()

    def create_widgets(self):
        create_label(self, "Введите грузоподъемность", 0, 0)
        self.ent1 = create_entry(self, 0, 1)
        create_button(self, "Найти", 0, 2, self.search)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def search(self):
        if hasattr(self, 'treeview'):
            self.treeview.delete(*self.treeview.get_children())
        try:
            capacity = float(self.ent1.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Введите число")
            return

        db = Database("transport.db")
        transports = db.get_transports()

        columns = ("name", "capacity", "length", "width", "height", "available")
        widths = (70, 120, 70, 70, 70, 70)
        headings = ("Название", "Грузоподъемность", "Длина", "Ширина", "Высота", "В наличии")
        self.treeview = create_treeview(self, columns, widths, headings)
        for transport in transports:
            if float(transport[2]) == capacity:
                self.treeview.insert("", "end", text=transport[0], values=transport[1:])

        db.close()
