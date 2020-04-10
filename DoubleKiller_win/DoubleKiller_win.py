#! python3
# -*- coding: utf-8 -*-
#       ДИСКОВЫЙ ОПТИМИЗАТОР
# определяет наличие файлов JPG, дублирующих RAW и удаляет JPG
import os, time, sys, datetime, re
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QPalette, QBrush, QColor, QFont
#импортируем графический интерфейс
from ui_DoubleKiller import Ui_Form

# функция диалога выбора папки
def pushButton_folder_dialog_funct(self):
    self.ui.pushButton.clicked.connect(self.folder_dialog)

def label_funkt(self):
    self.label = self.ui.label


#определяяем откуда будем наследовать диалоги
class MainWindowForFileDialog(QMainWindow):
    # строим конструктор диалогов
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        pushButton_folder_dialog_funct(self)
        label_funkt(self)


    def folder_dialog(self):
        dialog_name = 'Please choose some directory to open'
        folder_init_name = './'
        foldername = QFileDialog.getExistingDirectory(self, dialog_name, folder_init_name )
        # определяется папка, в которой ведется проверка
        # переменной tree передается функция, которая поделила путь на кортежи:
        # Первый – адрес каталога, второй – список его поддиректорий первого уровня,
        # третий – список имен файлов. Если вложенных каталогов или файлов нет,
        # соответствующий список пуст.
        tree = os.walk(foldername)
        #задаются исходные значения для результатов очистки
        d = 0
        f = 0
        doubleResult = []
        rawFiles = []
        # обнуляются исходные данные для функции подбора по расширениям
        #возвращается выражение уравнивающее написания расширения файла

        log_double_killer = open('log_double_killer.txt', 'a')
        self.ui.label.setText("Идет очистка")
        self.ui.label_2.setText("ждите")
        log_double_killer.write('\n'*3 + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + '\n')

        # задается функция подбора файлов в кортеж
        def baseFilesFunction(extension):
            baseFiles = []
            for file in files:
            #определяется: их ли это расширение? 
            #независимо от того заглавными или строчными оно записано
                if file.endswith("." + extension.upper()) or file.endswith("." + extension.lower()):
                # имена файлов записываются в переменную baseFiles
                    baseFiles.append(os.path.splitext(file)[0])
            return(baseFiles)

        # для всех файлов на проверяемом пути
        for address, dirs, files in tree:
            log_double_killer.write("-" * 30 + '\n')
           
            #находятся raw файлы с любым расширением при помощи функии endSwith
            rawExtention = ('ari', 'dpx', 'arw', 'srf', 'sr2', 'bay', 'crw', 'cr2', 'cr3', 'dng', 'dcr', 'kdc', 'erf', '3fr', 'mef', 'mrw', 'nef', 'nrw', 'orf', 'ptx', 'pef', 'raf', 'raw', 'rwl', 'dng', 'raw', 'rw2', 'r3d', 'srw', 'x3f')
            for extension in rawExtention:
                rawFiles = rawFiles + baseFilesFunction(extension)
            r = len(rawFiles)

            #находятся файлы с расширением jpg при помощи функии endSwith
            extension = 'jpg'
            jpgFiles = baseFilesFunction(extension)
            j = len(jpgFiles)
            f += 1   
            # сравниваются массивы и находятся общие имена файлов
            doubleFiles = set(jpgFiles).intersection(rawFiles)
            log_double_killer.write("В папке " + address + "\njpg файлов = " + str(j) + "\n" + "raw файлов = " + str(r) + "\nдублирующих файлов = " + str(len(doubleFiles)) + '\n')
            # сбросить счетчик 
            rawFiles = []

            for file in files:
                    # для всех jpg файлов на проверяемом пути, отмеченных в дублировании
                if((file.endswith('.JPG') or file.endswith('.jpg')) and
                   os.path.splitext(file)[0]) in doubleFiles:
                    #происходит удаление дублей
                    os.unlink(address + '\\' + file)
                    # или вывод на печать для проверки
                    #print(os.path.join(address + '/' + file))
                    log_double_killer.write(file + '\n')
                    d += 1
                    doubleResult.append(os.path.join(address))
                    time.sleep(1)
        log_double_killer.write("\n" + "=" * 10 + "\nпроверено папок = " + str(f) + ", вычищено дублей = " + str(d) + '\n')
        #texts = "проверено папок = " + str(f) + "\nвычищено дублей = " + str(d)

        doubleSet = set(doubleResult)
        for double in doubleSet:
            log_double_killer.write(double + '\n')

        log_double_killer.close()
        self.ui.label.setText("проверено папок = " + str(f) + "\nвычищено дублей = " + str(d))
        #Для того, чтобы вывести ссылку на лог
        path_log = os.getcwd() + '\\log_double_killer.txt'
        #В ссылке меняется обратный слеш на прямой
        path_rep = path_log.replace('\\' , '/')
        # формируется текст надписи
        path_log = 'лог очистки сохранен в файле: ' + '<a href="' + path_rep + '">' + path_log + '</a>'
        self.ui.label_2.setText(path_log)
        self.ui.label_2.setOpenExternalLinks(True)

# создаем основную функцию
def main():
    app = QApplication(sys.argv)
    main = MainWindowForFileDialog()
    main.show()
    app.exec_()

# запускаем основную функцию
if __name__ == '__main__':
    main()