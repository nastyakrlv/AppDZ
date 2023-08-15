from utility import *
from databaze import *


class ViewAllWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Просмотреть весь доступный транспорт")
        self.geometry("600x300")

        self.create_widgets()

    def create_widgets(self):
        self.db = Database("transport.db")
        columns = ("name", "capacity", "length", "width", "height", "available")
        widths = (70, 120, 70, 70, 70, 70)
        headings = ("Название", "Грузоподъемность", "Длина", "Ширина", "Высота", "В наличии")
        self.treeview = create_treeview(self, columns, widths, headings)

        self.transports = self.db.get_transports()
        for transport in self.transports:
            self.treeview.insert("", "end", text=transport[0], values=transport[1:])
        self.db.close()

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
