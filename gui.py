from addWindow import *
from delWindow import *
from viewallWindow import *
from viewbycapacityWindow import *
from availableWindow import *
from selectionbooking import *


# Класс приложения
class TransportApp(Tk):
    def __init__(self):
        super().__init__()
        self.title('Грузовой транспорт')
        self.geometry('820x200')

        # Создание графического интерфейса
        self.create_widgets()

    # Главная страница
    def create_widgets(self):
        create_label(self.master, "ГЛАВНОЕ МЕНЮ", 0, 1, 2)

        button_names = ["Добавить грузовой транспорт", "Удалить грузовой транспорт",
                        "Просмотреть весь доступный транспорт", "Просмотреть грузовой транспорт по грузоподъемности",
                        "Просмотреть свободный/занятый грузовой транспорт",
                        "Подобрать и забронировать транспорт"]
        commands = [self.add_window, self.del_window, self.view_all, self.view_by_capacity, self.available,
                    self.selection_booking]

        [create_button(self.master, button_names[(i - 1) * 2], i, 1, commands[(i - 1) * 2]) for i in range(1, 4)]
        [create_button(self.master, button_names[(i - 1) * 2 + 1], i, 2, commands[(i - 1) * 2 + 1]) for i in
         range(1, 4)]

    def add_window(self):
        window = AddWindow(self)
        window.grab_set()

    def del_window(self):
        window = DelWindow(self)
        window.grab_set()

    def view_all(self):
        window = ViewAllWindow(self)
        window.grab_set()

    def view_by_capacity(self):
        window = ViewByCapacityWindow(self)
        window.grab_set()

    def available(self):
        window = AvailableWindow(self)
        window.grab_set()

    def selection_booking(self):
        window = SelectionBookingWindow(self)
        window.grab_set()


if __name__ == "__main__":
    app = TransportApp()
    app.mainloop()
