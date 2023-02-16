# Лабораторная работа №3
# Вариант 8
import os
import csv
import datetime

mydicts = []        # Словарь
path = "lab3.csv"

# Сортировка различные варианты
def my_sort(mydicts, way_sort):
    if way_sort == 0:
        mydicts.sort(key=lambda x: int(x['id']))       # Сортировка по id
    elif way_sort == 1:
        mydicts.sort(key=lambda x: x['name_p'])        # Сортировка по имени пациента
    elif way_sort == 2:
        mydicts.sort(key=lambda x: x['name_d'])         # Сортировка по врача
    elif way_sort == 3:
        mydicts.sort(key=lambda x: x['reason'])         # Сортировка по причине обращения
    elif way_sort == 4:
        mydicts.sort(key=lambda x: x['time'])           # Сортировка по времени приёма (по возрастанию)
    else:
        print("Такого метода сортировки нет")
        quit()

# Функция для преобразовния секунд в формат минута:секунда
def get_format(seconds: int):
    minutes = str(seconds // 60)
    seconds = str(seconds % 60)

    if int(minutes) < 10:
        minutes = '0' + minutes
    if int(seconds) < 10:
        seconds = '0' + seconds

    return f"{minutes}:{seconds}"

# Функция для вывода записи
def format_print_dict(line):
    print(f"\nЗапись № {line['id']}:"
          f"\nПациент - {line['name_p']}"
          f"\nВрач - {line['name_d']}"
          f"\nПричина обращения - {line['reason']}"
          f"\nДлительность обращения - {line['time']}\n")


# Рычаги для управления программы
GET_COUNT_FILE_DIR = False      # Считать файлы в директории
WRITE_RECORD = False            # Сделать запись в csv файл
LOAD_RECORDS = True             # Загрузить записи
OUTPUT_RECORDS = True           # Вывести записи, выбрав сбособ сортировки. LOAD_RECORS должен быть True
SELECT_RECORDS = False          # Вывести записи по одному из критериев. LOAD_RECORS должен быть True

if __name__ == "__main__":

    if GET_COUNT_FILE_DIR:
        try:
            path = input("Введите путь директории(папки): ")
            # root - имя корневого каталога
            # dirs - список имен вложенных папок
            # files - список файлов в текущем каталоге
            root, dirs, files = next(os.walk(path))     # Выдаёт тройной кортеж - (dirpath, dirnames, filenames)
                                                        # возвращающает имена файлов в дереве каталогов, двигаясь по дереву сверху вниз
            print("Количество файлов в данной директории: ", len(files))
        except FileNotFoundError:
            print("Директория с таким путём не найдена...")
            quit()

    if WRITE_RECORD:
        name_patient = input("ФИО пациента: ")
        name_doc = input("ФИО врача: ")
        reason = input("Причина обращения: ")
        diraction = int(input("Длительность приёма(сек): "))
        time = get_format(diraction)
        idx = datetime.datetime.now().strftime("%d%H%M%S")

        line = {'id': idx, 'name_p': name_patient, 'name_d': name_doc, 'reason': reason, 'time': time}
        print(f"Записи присвоен № {line['id']}.")

        with open(path, "a", newline="") as file:
            writer = csv.DictWriter(file,  fieldnames=['id', 'name_p', 'name_d', 'reason', 'time'])       # Объект писателя, с помощью которого и записываем файл
            writer.writerow(line)         # Сделать запись
            file.close()

    if LOAD_RECORDS:
        with open(path, "r") as tabel_file:
            reader = csv.DictReader(tabel_file, fieldnames=['id', 'name_p', 'name_d', 'reason', 'time'])
            for record in reader:
                mydicts.append(dict(record))

        if OUTPUT_RECORDS:
            print("Отсоритровать записпи по\n0 - id\n1 - ФИО пациента\n"
                  "2 - ФИО врача\n3 - причине обращения\n4 - длительности посещения")
            way = int(input())
            my_sort(mydicts, way)

            for line in mydicts:
                format_print_dict(line)

        if SELECT_RECORDS:
            for line in mydicts:
                if(line['reason'] == "Temperature"):
                    format_print_dict(line)