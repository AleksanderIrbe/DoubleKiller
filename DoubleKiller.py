#! python3
# -*- coding: utf-8 -*-
#       ДИСКОВЫЙ ОПТИМИЗАТОР
# определяет наличие файлов JPG, дублирующих RAW и удаляет JPG
import os, time
# устанавливается модуль для работы с операционной системой
workDir = input(os.path.join(u"Введите путь к директории : >> "))
# определяется папка, в которой ведется проверка
# переменной tree передается функция, которая поделила путь на кортежи:
# Первый – адрес каталога, второй – список его поддиректорий первого уровня,
# третий – список имен файлов. Если вложенных каталогов или файлов нет,
# соответствующий список пуст.
tree = os.walk(workDir)
#задаются исходные значения для результатов очистки
d = 0
doubleResult = []
# обнуляются исходные данные для функции подбора по расширениям
#возвращается выражение уравнивающее написания расширения файла

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
    print("-" * 30)
   
    #находятся файлы с расширением cr2 при помощи функии endSwith
    extension = 'cr2'
    cr2Files = baseFilesFunction(extension)
    r = len(cr2Files)

    #находятся файлы с расширением jpg при помощи функии endSwith
    extension = 'jpg'
    jpgFiles = baseFilesFunction(extension)
    j = len(jpgFiles)
        
    # сравниваются массивы и находятся общие имена файлов
    doubleFiles = set(jpgFiles).intersection(cr2Files)
    print("В папке ", address, "\njpg файлов = ", j, "\nraw файлов = ", r)
    print("дублирующих файлов = ", len(doubleFiles))
    

    for file in files:
            # для всех jpg файлов на проверяемом пути, отмеченных в дублировании
        if((file.endswith('.JPG') or file.endswith('.jpg')) and
           os.path.splitext(file)[0]) in doubleFiles:
            #происходит удаление дублей
            #os.unlink(os.path.join(address + '\\' + file))
            os.unlink(address + '\\' + file)
            # или вывод на печать для проверки
            #print(os.path.join(address + '\\' + file))
            d += 1
            doubleResult.append(os.path.join(address))
            time.sleep(1)
print("\n", "=" * 10, "\nвычищено дублей =", d, "\nв директориях:")
doubleSet = set(doubleResult)
for double in doubleSet:
    print(double)