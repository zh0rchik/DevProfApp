# Лабораторная работа №1. Работа со списком
# Вариант 8
import random

def generate_random_list(left, right, size):
    list = []
    for i in range(size):
        list.append(random.randint(left, right))   # Метод, который возвращает случайное число в заданном диапозоне
    return list

def get_len_list(list):
    count = 0
    for i in list:
        count += 1
    return count

def existence(element, list):                     # Функция проверки наличия элемента (аналог in)
    for i in list:
        if i == element:
            return True
    return False

print("0 - для ввода переменных с клавиатуры"       
      "\n1 - для генерации переменных")
w = int(input())

if w != 0 and w != 1:
    print("Нет такого ответа...")

a, b = [], []

if not(bool(w)):
    # Наполнение множества А. map
    a = list(map(int, input().split()))
    # Наполнение множества B. map
    b = list(map(int, input().split()))
else:
    # Наполнение множеств случайными числами
    a, b = generate_random_list(0, 9, 10), generate_random_list(0, 9, 5)
    print(a)
    print(b)

if get_len_list(a) == 0 or get_len_list(b) == 0:
    print("Один из списков пустой...")
    quit()
# Список, содержащий ключи элементов подпоследователности в множестве А
seq = []
# Список из seq
sequences = []

# Добавление цепочек
for i in range(get_len_list(a)):
    if a[i] % 2 != 0:
        # Добавление элемента в одну из цепочек
        seq.append(i)
        if i == get_len_list(a) - 1:
            sequences.append(list(seq))               # Метод list() позволяет запушить список в список.
            seq.clear()                               # Очищение списка
    elif get_len_list(seq) != 0:
        sequences.append(list(seq))
        seq.clear()

# Удаление цепочек
count_deleted_elements = 0                              # Кол-во удалённых элементов, требуется для вычисления индекса
for s in sequences:                                     # foreach для прождения списком по списку из список
    flag = False
    for i in s:                                         # foreach для прождению списку ключей одной из цепочек
        if existence(a[i - count_deleted_elements], b): # При удалении элемента индекс последующих меняется, но он не меняется в списках
            flag = True                                 # Флаговая меняет своё значение, если находит элемент содержится в B,
            break
    if not(flag):
        for j in s:
            a.pop(j - count_deleted_elements)
            count_deleted_elements += 1

print(a)