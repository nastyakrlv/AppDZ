from utility import *
from databaze import Database


class AvailableWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Просмотреть свободный/занятый грузовой транспорт")
        self.geometry("560x250")

        self.create_widgets()

    def create_widgets(self):

        self.radio_var = IntVar()
        self.radio_var.set(1)
        radio_button_1 = Radiobutton(self, text="Просмотреть свободный транспорт",
                                          variable=self.radio_var, value=1, command=self.show_available)
        radio_button_2 = Radiobutton(self, text="Просмотреть занятый транспорт",
                                          variable=self.radio_var, value=0, command=self.show_no_available)
        radio_button_1.grid(row=0, column=0)
        radio_button_2.grid(row=0, column=1)

        columns = ("name", "capacity", "length", "width", "height", "available")
        widths = (100, 120, 70, 70, 70, 70)
        headings = ("Название", "Грузоподъемность", "Длина", "Ширина", "Высота", "В наличии")
        self.treeview = create_treeview(self, columns, widths, headings)

        self.show_available()

    def show_available(self):
        self.treeview.delete(*self.treeview.get_children())
        db = Database("transport.db")
        transports = db.get_transports()
        for transport in transports:
            if transport[-1] == 1:
                self.treeview.insert("", "end", text=transport[0], values=transport[1:])
        db.close()

    def show_no_available(self):
        self.treeview.delete(*self.treeview.get_children())
        db = Database("transport.db")
        transports = db.get_transports()
        for transport in transports:
            if transport[-1] == 0:
                self.treeview.insert("", "end", text=transport[0], values=transport[1:])
        db.close()
