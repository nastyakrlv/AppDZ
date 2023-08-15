from tkinter import messagebox
from tkinter.ttk import Combobox
from utility import *
import re
from databaze import Database


class AddWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Добавить грузовой транспорт")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        label_names = ["Название", "Грузоподъемность", "Длина", "Ширина", "Высота"]
        [create_label(self, label_names[i - 1], i, 1) for i in range(1, 6)]

        transport = ['Газель', 'Бычок', 'Фура', 'MAN-10']
        self.var = StringVar(value=transport[0])
        self.combobox = Combobox(self, values=transport, textvariable=self.var, state="readonly")
        self.combobox.grid(row=1, column=2, padx=10, pady=10)

        self.entries = [create_entry(self, i, 2) for i in range(2, 6)]
        create_button(self, "Добавить", 6, 1, self.add, 2)

    def add(self):
        values = [entry.get() for entry in self.entries]
        capacity, length, width, height = values
        name = self.combobox.get()

        # Проверка на то что переменные - числа
        try:
            [float(value) for value in values]
        except ValueError:
            messagebox.showerror('Ошибка', 'Грузоподъемность, длина, ширина и высота должны быть числами.')
            return
        db = Database('transport.db')
        lim = db.get_limitations_by_name(name)
        if not (all(lim[i * 2] <= float(values[i]) <= lim[i * 2 + 1] for i in range(len(values)))):
            messagebox.showerror('Ошибка', 'Значение должно соответствовать ограничениям.')
        else:
            db.add_transport(name, capacity, length, width, height, 1)
            messagebox.showinfo('Успешно', f'Транспорт "{name}" добавлен в базу данных!')
        db.close()

        # db = Database('transport.db')
        # db.add_limitation("Газель", 2, 2, 3, 3, 2, 2, 1.7, 2.2)
        # db.add_limitation("Бычок", 3, 3, 4.2, 5, 2, 2.2, 2, 2.4)
        # db.add_limitation("MAN-10", 10, 10, 6, 8, 2.45, 2.45, 2.3, 2.7)
        # db.add_limitation("Фура", 20, 20, 13.6, 13.6, 2.46, 2.46, 2.5, 2.7)
