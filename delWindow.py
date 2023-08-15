from utility import *
from tkinter import ttk
from databaze import Database
from tkinter import messagebox


class DelWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Удалить грузовой транспорт")
        self.geometry("600x300")

        self.create_widgets()

    def create_widgets(self):

        self.db = Database("transport.db")
        self.transport_ids = [str(transport[0]) for transport in self.db.get_transports()]
        # Если база данных не пустая
        if len(self.transport_ids) > 0:
            self.selected_transport = StringVar()
            self.selected_transport.set(self.transport_ids[0])
            self.dropdown = OptionMenu(self, self.selected_transport, *self.transport_ids)
            self.dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=W)

            self.label = create_label(self, "Выберите ID транспорта:", 0, 0)
            self.delete_button = create_button(self, "Удалить", 0, 2, self.delete_transport)
        # Если база данных пустая
        else:
            create_label(self, "Нет транспорта в базе данных", 0, 0)
        # Создание таблицы
        columns = ("name", "capacity", "length", "width", "height", "available")
        widths = (70, 120, 70, 70, 70, 70)
        headings = ("Название", "Грузоподъемность", "Длина", "Ширина", "Высота", "В наличии")
        self.treeview = create_treeview(self, columns, widths, headings)

        # Настройка окна
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.load_data()
        self.db.close()

    # Обновление и заполнение талицы
    def load_data(self):
        self.treeview.delete(*self.treeview.get_children())
        self.transports = self.db.get_transports()
        for transport in self.transports:
            self.treeview.insert("", "end", text=transport[0], values=transport[1:])

    def delete_transport(self):

        self.db = Database("transport.db")
        # Получаем ID выбранного транспорта
        transport_id = int(self.selected_transport.get())

        if len(self.transport_ids) > 0:
            # Удаляем транспорт из базы данных
            self.db.delete_transport(transport_id)
            # Обновляем выпадающий список и таблицу со списком транспорта
            self.transports = self.db.get_transports()
            self.transport_ids = [str(transport[0]) for transport in self.transports]
            if len(self.transport_ids) > 0:
                self.selected_transport.set(self.transport_ids[0])
                self.dropdown['menu'].delete(0, 'end')
                for id in self.transport_ids:
                    self.dropdown['menu'].add_command(label=id,
                                                      command=lambda value=id: self.selected_transport.set(value))
            else:
                self.selected_transport.set("")
                self.dropdown.grid_remove()
                self.delete_button.grid_remove()
                self.label.config(text="Нет транспорта в базе данных")
            self.load_data()
            messagebox.showinfo("Удаление транспорта", f"Транспорт с ID={transport_id} удален из базы данных.")
            self.db.close()
