from utility import *
from tkinter import messagebox
from databaze import *


class SelectionBookingWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Внести заявку на перевоз груза по указанным габаритам")
        self.geometry("350x400")

        self.create_widgets()

    def create_widgets(self):
        label_names = ["Вес груза", "Длина", "Ширина", "Высота"]
        [create_label(self, label_names[i], i, 0) for i in range(4)]

        self.entries = [create_entry(self, i, 1) for i in range(4)]
        create_button(self, "Подобрать", 4, 0, self.select)

    def select(self):
        values = [entry.get() for entry in self.entries]
        try:
            values = [float(value) for value in values]
        except ValueError:
            messagebox.showerror('Ошибка', 'Грузоподъемность, длина, ширина и высота должны быть числами.')
            return

        db = Database("transport.db")
        transports = db.get_transports()
        self.transports_list = []

        for transport in transports:
            if all([transport[i+2] >= values[i] for i in range(len(values))]) and transport[6] == 1:
                self.transports_list.append(transport)

        if not self.transports_list:
            messagebox.showinfo('Внимание', 'Подходящего транспорта не найдено.')
            return

        self.transport_vars = [IntVar() for _ in self.transports_list]

        for i, transport in enumerate(self.transports_list):
            cb = Checkbutton(self,
                             text=f"{transport[1]} ({transport[3]}x{transport[4]}x{transport[5]}), Грузоподъемность: {transport[2]} кг.",
                             variable=self.transport_vars[i])
            cb.grid(row=5 + i, column=0, columnspan=2)

        create_button(self, "Забронировать", 4, 1,
                      self.add_transport)
        db.close()

    def add_transport(self):
        selected_transports = [transport[0] for i, transport in enumerate(self.transports_list) if
                               self.transport_vars[i].get() == 1]
        if not selected_transports:
            messagebox.showinfo('Внимание', 'Транспорт не выбран.')
            return
        db = Database("transport.db")
        for transport in selected_transports:
            db.mark_transport_unavailable(transport)
        messagebox.showinfo('Успешно', 'Транспорт успешно забронирован')
        self.destroy()
