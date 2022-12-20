from tkinter import *
# from tkinter import ttk
from tkinter.ttk import *
from create import Create
import pygame
from PIL import ImageTk, Image

class Programm():
    def __init__(self):
        self.window = Tk()
        self.window.title("Создание магических квадратов")
        self.window.geometry('1000x561')
        self.menu()
        # self.window.resizable(False, False)

        pygame.init()
        self.song = pygame.mixer.Sound('images/Смешарики.mp3')
        self.song.play()
        self.window.mainloop()

    # менюшка
    def menu(self):
        self.size = self.image_size('images/Frame 1.png')
        self.image = ImageTk.PhotoImage(self.size)
        self.panel = Label(self.window, image = self.image)
        # self.panel.pack()
        # self.panel.pack(side="top", fill="both", expand="no")
        self.panel.pack(side="top", fill=BOTH, expand=1)
        
        self.button_create = Button(self.window, text = "Создать", command = lambda: [self.clean_data(
                [self.panel, self.button_create, self.button_settings, self.button_about]),
                self.create()
            ])
        self.button_settings = Button(self.window, text = "Настройки", command = lambda: [self.clean_data(
                [self.panel, self.button_create, self.button_settings, self.button_about]),
                self.settings()
            ])
        self.button_about = Button(self.window, text = "О приложении", command = lambda: [self.clean_data(
                [self.panel, self.button_create, self.button_settings, self.button_about]),
                self.about_program()
            ])

        self.data = Entry(self.window, width=10)
        
        self.button_create.place(relx = 0.435, rely = 0.435)
        self.button_settings.place(relx = 0.435, rely = 0.585)
        self.button_about.place(relx = 0.435, rely = 0.735)

    # вкладка создания квадрата
    def create(self):
        self.size = self.image_size('images/Frame 2.png')
        self.image = ImageTk.PhotoImage(self.size)
        self.panel = Label(self.window, image = self.image)
        self.panel.pack(side="top", fill=BOTH, expand=1)
        
        self.data = Entry(self.window, width=10)
        self.data.pack()

        self.back_button = Button(self.window, text = "Назад", command = lambda: [
                self.clean_data([self.panel, self.data, self.do_button, self.back_button]),
                self.menu(),
            ])
        self.do_button = Button(self.window, text = "Создать", command = lambda: [self.create_square(),
                self.clean_data([self.panel, self.data, self.do_button, self.back_button])
            ])
        self.back_button.pack(side = BOTTOM)
        self.do_button.pack(side = BOTTOM)

    # вкладка о программе
    def about_program(self):
        self.size = self.image_size('images/mulyadi-TyjFLWdZris-unsplash 1.png')
        self.image = ImageTk.PhotoImage(self.size)
        self.panel = Label(self.window, image = self.image)
        self.panel.pack(side=TOP, fill="both", expand="no")

        self.text = "Данно приложение предназначено для создания магического квадрата в разных вариациях. \
            Запомните, программа способна создать квадрат только из положительных целых чисел. Аналогов \
                данной программы нет, поэтому пользуйтесь, дорогие уроды =)"
        self.result = self.display()
        self.txt1 = Label(self.window, text = self.text, wraplength = self.result)
        self.txt1.pack(side = TOP)
        self.auther = "Программа разработана Гайдымом Н.А. по заказу УО БГУИР филиал МРК"
        self.txt2 = Label(self.window, text = self.auther)
        self.txt2.pack(side = BOTTOM)
        self.back_button = Button(self.window, text  = "В главное меню", command = lambda:[self.clean_data(
                [self.panel, self.txt1, self.txt2, self.back_button]),
                self.menu()
            ])
        self.back_button.pack(side = BOTTOM)

    # вкладка настройки
    def settings(self):
        self.size = self.image_size('images/Frame 4.png')
        self.image = ImageTk.PhotoImage(self.size)
        self.panel = Label(self.window, image = self.image)
        self.panel.pack(side=TOP, fill="both", expand="no")

        self.rad_music_play = Radiobutton(self.window, value=1, state = "disabled",
            command = lambda: [self.play_music(), self.switch()])  
        self.rad_music_off = Radiobutton(self.window, value=2,
            command = lambda: [pygame.quit(), self.switch()])

        self.rad_music_play.place(relx = 0.12, rely = 0.56)
        self.rad_music_off.place(relx = 0.365, rely = 0.56)
        # self.rad_music_off.pack()
        
        
        # self.scale = Scale(self.window, orient=HORIZONTAL, from_=0, to=100)
        # self.scale.pack(side=LEFT, padx=15)
        # self.scale.bind("<B1-Motion>", self.func)
        
        self.back_button = Button(self.window, text  = "В главное меню", command = lambda:[self.clean_data(
                [self.panel, self.rad_music_play, self.rad_music_off , self.back_button]),
                self.menu()
            ])
        self.back_button.pack(side = BOTTOM)

    # удаление мусора
    def clean_data(self, *args):
        for arg in args:
            for object_name in arg:
                object_name.destroy()

    # вывод квадрата с кнопкой пересоздания
    def draw_square(self, n, *args):
        try:
            self.clean_data(self.values)
        except:
            self.values = []    # переменная для мусора
        kol = 0
        down = 10
        for arg in args:
            for elements in arg:
                if kol % n == 0:
                    down += 10
                a1 = Label(self.window, text = elements, font="Times 20")
                a1.pack(ipady = down)
                self.values.append(a1)

        self.recreate_button = Button(self.window, text = "Пересоздать", command = lambda: [self.create_square()])
        self.recreate_button.pack(side = BOTTOM)
        # добавляем кнопку в переменную для мусора
        self.values.append(self.recreate_button)

    # создания магического квадрата
    def create_square(self):
        # первое создание квадрата
        try:
            self.value = self.data.get()
            self.square = Create(int(self.value))
            result = self.square.generateSquare()
            self.draw_square(int(self.value), result)
        # пересоздаем квадрат
        except:
            result = self.square.generateSquare()
            self.draw_square(int(self.value), result)

    def image_size(self, path):
        self.image = Image.open(path)
        self.width = 1000
        self.ratio = (self.width / float(self.image.size[0]))
        self.height = int((float(self.image.size[1]) * float(self.ratio)))
        self.size = self.image.resize((self.width, self.height), Image.ANTIALIAS)
        return self.size

    def display(self):
        self.window_width = self.window.winfo_width()
        self.wrapLen = self.window_width/3
        return self.wrapLen

    def play_music(self):
        pygame.init()
        self.song = pygame.mixer.Sound('images/Смешарики.mp3')
        self.song.play()

    # функция для активации/деактивации кнопок музыки
    def switch(self):
        if self.rad_music_play["state"] == "disabled":
            self.rad_music_play["state"] = "normal"
            self.rad_music_off["state"] = "disabled"
        elif self.rad_music_off["state"] == "disabled":
            self.rad_music_play["state"] = "disabled"
            self.rad_music_off["state"] = "normal"



a = Programm()