import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
        QVBoxLayout, QGridLayout, QRadioButton, QLineEdit, QHBoxLayout, QScrollArea, QGroupBox)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import pygame
from math import sqrt
from create import Create

class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainwindow")

        self.widget = QWidget(self)
        self.widget.setObjectName("widget")

        self.layout = QGridLayout(self.widget)

        self.play_music()

        self.menu()

    # менюшка
    def menu(self):
        self.setStyleSheet('''
            #widget {
                border-image: url(images/Frame 1.png) 0 0 0 0;
            }
            #label {
                color: #fff;
            }
        ''')

        self.label = QLabel(alignment=Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label1 = QLabel("")
        self.label2 = QLabel("")
        self.label3 = QLabel("")
        self.label4 = QLabel("")
        self.label5 = QLabel("")
        self.label6 = QLabel("")
        self.label7 = QLabel("")
        self.label8 = QLabel("")
        self.label9 = QLabel("")

        self.button_create = QPushButton('Создать')
        self.button_create.setObjectName("button_create")
        self.button_create.clicked.connect(lambda: [
            self.clean_data([
                self.button_create, 
                self.button_settings, 
                self.button_about,
                self.label1,
                self.label2,
                self.label3,
                self.label4,
                self.label5,
                self.label6,
                self.label7,
                self.label8,
                self.label9,
                ]),
            self.create()
        ])
        self.layout.addWidget(self.button_create, 5, 1, 1, 1)
        
        self.button_settings = QPushButton('Настройки')
        self.button_settings.setObjectName("button_settings")
        self.button_settings.clicked.connect(lambda: [
            self.clean_data([
                self.button_create, 
                self.button_settings, 
                self.button_about,
                self.label1,
                self.label2,
                self.label3,
                self.label4,
                self.label5,
                self.label6,
                self.label7,
                self.label8,
                self.label9,
                ]),
            self.settings()
        ])
        # self.vbox1.addWidget(self.button_settings)
        self.layout.addWidget(self.button_settings, 7, 1, 1, 1)
        
        self.button_about = QPushButton("О программе")
        self.button_about.setObjectName("button_about")
        self.button_about.clicked.connect(lambda: [
            self.clean_data([
                self.button_create, 
                self.button_settings, 
                self.button_about,
                self.label1,
                self.label2,
                self.label3,
                self.label4,
                self.label5,
                self.label6,
                self.label7,
                self.label8,
                self.label9,
                ]),
            self.about_program()
            ])
        self.layout.addWidget(self.button_about, 9, 1, 1, 1)

        self.layout.addWidget(self.label1, 1, 1, 1, 1)
        self.layout.addWidget(self.label2, 2, 1, 1, 1)
        self.layout.addWidget(self.label3, 3, 1, 1, 1)
        self.layout.addWidget(self.label4, 4, 1, 1, 1)
        self.layout.addWidget(self.label5, 6, 1, 1, 1)
        self.layout.addWidget(self.label6, 8, 1, 1, 1)
        self.layout.addWidget(self.label7, 10, 1, 1, 1)
        self.layout.addWidget(self.label8, 11, 1, 1, 1)
        self.layout.addWidget(self.label9, 0, 1, 1, 1)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.widget)

    # вкладка создания квадрата
    def create(self):
        self.setStyleSheet('''
            #widget {
                border-image: url("images/Frame 2.png") 0 0 0 0;
            }
            #label {
                color: #fff;
            }
        ''')

        # для кнопок
        self.vbox1 = QVBoxLayout(spacing = 3)
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()

        # не трогать (для выравнивания)
        self.label1 = QLabel("")
        self.label2 = QLabel("")
        self.vbox4 = QVBoxLayout()
        self.vbox5 = QVBoxLayout()

        self.field = QLineEdit()
        self.field.setObjectName("field")
        self.field.setFixedWidth(200)
        self.field.setFixedHeight(30)
        self.vbox1.addWidget(self.field)

        self.create_button = QPushButton("Создать")
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(lambda: [
            self.clean_data([
                self.field,
                self.create_button,
                self.back_button,
                self.history_button,
                self.vbox1,
                self.vbox2,
                self.vbox3,
                self.label1,
                self.label2,
                self.vbox4,
                self.vbox5,
            ]),
            self.create_square(),
        ])
        self.vbox1.addWidget(self.create_button)

        self.vbox4.addWidget(self.label1)
        self.vbox5.addWidget(self.label2)

        self.history_button = QPushButton("История")
        self.history_button.setObjectName("history_button")
        self.history_button.clicked.connect(lambda: [
            self.clean_data([
                self.field,
                self.create_button,
                self.back_button,
                self.history_button,
                self.vbox1,
                self.vbox2,
                self.vbox3,
                self.label1,
                self.label2,
                self.vbox4,
                self.vbox5,
            ]),
            self.history("read"),
        ])
        self.vbox2.addWidget(self.history_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda: [
            self.clean_data([
                self.field,
                self.create_button,
                self.back_button,
                self.history_button,
                self.vbox1,
                self.vbox2,
                self.vbox3,
                self.label1,
                self.label2,
                self.vbox4,
                self.vbox5,
            ]),
            self.menu()
        ])
        self.vbox3.addWidget(self.back_button)

        self.layout.addLayout(self.vbox4, 0, 0)
        self.layout.addLayout(self.vbox5, 2, 0)

        self.layout.addLayout(self.vbox1, 1, 0, alignment=Qt.AlignVCenter)
        self.layout.addLayout(self.vbox2, 0, 2, alignment=Qt.AlignTop)
        self.layout.addLayout(self.vbox3, 5, 1)

    # вкладка настройки
    def settings(self):
        self.vbox1 = QVBoxLayout()
        self.vbox1.addStretch(1)
        self.vbox2 = QVBoxLayout()
        
        self.central_labels = self.central_elements(12)

        self.hbox = QHBoxLayout()

        self.setStyleSheet('''
            #widget {
                border-image: url("images/Frame 4.png") 0 0 0 0;
            }
            #label {
                color: #fff;
            }
        ''')
        self.hbox.addWidget(self.label1)

        self.rad_music_play = QRadioButton("Вкл")
        self.rad_music_play.setChecked(True)
        self.rad_music_play.toggled.connect(lambda: [self.play_music()])  
        self.hbox.addWidget(self.rad_music_play)
        
        self.rad_music_off = QRadioButton("Выкл")
        self.rad_music_off.toggled.connect(lambda: [pygame.quit()])
        self.hbox.addWidget(self.rad_music_off)
        
        self.back_button = QPushButton('Назад')
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda: [
            self.clean_data([
                self.rad_music_play,
                self.rad_music_off,
                self.back_button,
                self.vbox1,
                self.vbox2,
                self.hbox,
                self.central_labels,
            ]),
            self.menu()
        ])
        self.vbox1.addWidget(self.back_button)

        self.layout.addLayout(self.central_labels, 0, 2)
        self.layout.addLayout(self.hbox, 1, 0, alignment=Qt.AlignBottom)
        self.layout.addLayout(self.vbox1, 2, 1)


    # вкладка о программе
    def about_program(self):
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox2.addStretch(1)

        self.setStyleSheet('''
            #widget {
                border-image: url("images/Frame 5.png") 0 0 0 0;
            }
            #label {
                color: #fff;
            }
        ''')

        self.label.setText(
            'В одном из приведённых ниже слов допущена ошибка в \nпост'
            'ановке ударения: НЕВЕРНО выделена буква, \nобозначающая '
            'ударный гласный звук. Выпишите это слово.')

        # не трогать (для выравнивания)
        self.central_labels = self.central_elements(8)
        self.central_labels.addWidget(self.label)

        self.back_button = QPushButton("Назад")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda: [
            self.clean_data([
                self.label,
                self.back_button,
                self.vbox1,
                self.vbox2,
                self.central_labels,
            ]),
            self.menu()
        ])
        self.vbox2.addWidget(self.back_button)

        self.layout.addLayout(self.central_labels, 0, 0, alignment=Qt.AlignBottom)
        self.layout.addLayout(self.vbox2, 1, 0, alignment=Qt.AlignCenter)

    # создания магического квадрата
    def create_square(self):
        # первое создание квадрата
        try:
            self.value = self.field.text()
            try:
                self.square = Create(int(self.value))
                result = self.square.generateSquare()
                self.draw_square(int(self.value), result)
            except:
                AnotherWindow(self, error = "error", fill = "None")
        # пересоздаем квадрат
        except:
            result = self.square.generateSquare()
            self.history("write", result)
            self.draw_square(int(self.value), result)

    # вывод квадрата с кнопкой пересоздания
    def draw_square(self, n, *args):
        kol = 0
        data = ''
        for arg in args:
            for ar in arg:
                self.var = QHBoxLayout(spacing = 5)
                self.var.addStretch(1)
                stroka = ''
                for i in ar:
                    self.var.addWidget(QLabel(f"{i}"))
                    stroka += str(i) + ' '
                data += stroka
                self.layout.addLayout(self.var, 0 + kol, 0)
                kol += 1
        self.setStyleSheet('''
            #widget {
                border-image: url("images/Frame 3.png") 0 0 0 0;
            }
            QLabel{
                color: #fff;
            }
        ''')
        self.history("write", data)

    # история
    def history(self, point, res = None):
        # вывести историю
        if point == "read":
            try:
                with open("data.txt", "r") as file:
                    self.all_data = []
                    while True:
                        buf = file.readline()
                        if buf == "":
                            break
                        else:
                            self.all_data.append(buf[0 : len(buf) - 1])
                    self.all_data.reverse()
                    kol = 0
                    self.data = []
                    for i in self.all_data:
                        if kol != 10:
                            self.data.append(i)
                            kol += 1
                    AnotherWindow(self, self.data)
                    # self.all_data.clear()
                    # self.data.clear()
            # исключение, если истории нет
            except FileNotFoundError:
                AnotherWindow(self)
        # запись в историю
        else:
            # запись
            try:
                with open("data.txt", "a") as file:
                    file.write(str(res))
                    file.write("\n")
            # создание файла
            except FileNotFoundError:
                with open("data.txt", "w") as file:
                    file.write(str(res))
                    file.write("\n")

    # удаление мусора
    def clean_data(self, *args):
        for arg in args:
            for object_name in arg:
                object_name.deleteLater()

    # запуск музыки
    def play_music(self):
        pygame.init()
        self.song = pygame.mixer.Sound('images/Смешарики.mp3')
        self.song.play()

    def central_elements(self, n):
        vbox1 = QVBoxLayout()
        for i in range(n):
            vbox1.addWidget(QLabel(""))
        return vbox1


# окно для вывода истории
class AnotherWindow(Program):
    def __init__(self, self2, fill = None, error = None):
        global c
        c = self2

        super(QWidget, self).__init__()
        self.setObjectName("infowindow")
        self.resize(500, 200)

        self.widget = QWidget(self)
        # self.widget.setObjectName("widget_info")

        self.layout2 = QGridLayout(self.widget)

        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox2.addStretch(1)

        if fill is None:
            self.history_window()
        elif error == "error":
            self.error_window()
        else:
            self.history_window(fill)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.widget)  

    def history_window(self, fill = None):
        if fill is None:
            self.label_info = QLabel("У вас нет истории", alignment=Qt.AlignCenter)
            self.vbox1.addWidget(self.label_info)
            # self.label_info.move(170, 20)

            self.back_button = QPushButton('Закрыть')
            self.back_button.setObjectName("back_button")
            self.back_button.clicked.connect(lambda: [
                self.close(),
                ])
            self.vbox2.addWidget(self.back_button)
            # self.back_button.move(110, 140)

            self.layout2.addLayout(self.vbox1, 0, 0, alignment=Qt.AlignTop)
            self.layout2.addLayout(self.vbox2, 0, 0, alignment=Qt.AlignCenter)
        else:
            self.vbox3 = QVBoxLayout(self)
            self.scroll = QScrollArea()
            
            self.back_button = QPushButton('Закрыть')
            self.back_button.setObjectName("back_button")
            self.back_button.clicked.connect(lambda: [
                self.close(),
                ])
            self.vbox2.addWidget(self.back_button)

            self.groupBox = QGroupBox()
            for arg in fill:
                data = []
                stroka = buf = ''
                for i in arg:
                    if i != ' ':
                        buf += i
                    else:
                        data.append(buf)
                        buf = ''
                barer = sqrt(len(data))
                barer = int(barer)
                self.vbox1.addWidget(QLabel(f"Магический квадрат числа {barer}"))
                for next, i in enumerate(data, start = 1):
                    stroka += str(i) + " "
                    if next % barer == 0:
                        self.vbox1.addWidget(QLabel(stroka))
                        stroka = ''
            
            self.groupBox.setLayout(self.vbox1)

            self.scroll.setWidget(self.groupBox)
            self.scroll.setWidgetResizable(True)
            
            self.vbox3.addWidget(self.scroll)

            self.layout2.addLayout(self.vbox3, 1, 0, alignment=Qt.AlignCenter)
            self.layout2.addLayout(self.vbox2, 0, 1, alignment=Qt.AlignTop)      
        self.show()

    def error_window(self):
        self.label = QLabel("Вводимые данные не являются числом.\nВводятся только числа!", 
            alignment=Qt.AlignCenter)
        self.vbox1.addWidget(self.label)

        self.back_button = QPushButton('Закрыть')
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda: [
            self.close(),
            ])
        self.vbox2.addWidget(self.back_button)

        self.layout2.addLayout(self.vbox1, 0, 0, alignment=Qt.AlignTop)
        self.layout2.addLayout(self.vbox2, 0, 0, alignment=Qt.AlignCenter)
        self.show()

    def closeEvent(self, event):
        self.close()
        c.create()



QSS = '''
#mainwindow {
    background-color: #000000;
}
#mainwindow2 {
    background-color: #105652;
}
#label {
    color: #fff;
    font-size: 24px;
}
#field {
    border: 2px solid gray;
    border-radius: 10px;
    padding: 0 8px;
}
QPushButton {
    background-image : url(images/Rectangle 9.png);
    border-style: outset;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
    min-width:  280px;
    max-width:  280px;
    min-height: 35px;
    max-height: 35px;
}
QPushButton:hover {
    background-color: #565612;
}
QRadioButton::indicator {
    width: 25px;
    height: 25px;
}
#widget {
    border-image: url("images/Frame 1.png") 0 0 0 0;
}
'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)
    ex = Program()
    ex.resize(1000, 561)
    ex.setWindowTitle('Крутое приложение')
    ex.setWindowIcon(QIcon('im.png'))
    ex.show()
    sys.exit(app.exec_())