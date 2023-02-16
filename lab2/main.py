# Лабораторная работа №2
# Вариант №8
import numpy

path_source = "source.txt"      # Путь исходника
path_processing_source = "processing_source.txt"            # Путь файла для записи обработки

# Функция для записи значения элемента матрицы в файл
def write_value_file(file, value):
    if value >= 0:
        file.write(' ' + str(value) + ' ')  # Запись элемента массива в файл
    else:
        file.write(str(value) + ' ')  # Запись элемента массива в файл

# Функция подсчёта количество отрицательных значений в строке
def count_negative_value_row(matrix, number_row, count_column):
    count = 0
    for j in range(count_column):
        if matrix[number_row][j] < 0:
            count += 1
    return count

# Функция подсчёта количество отрицательных значений в столбце
def count_negative_value_column(matrix, number_column, count_row):
    count = 0
    for i in range(count_row):
        if matrix[i][number_column] < 0:
            count += 1
    return count

if __name__ == "__main__":
    a = []                # Матрица
    n = int(input())      # Количество строк матрицы
    m = int(input())      # Количество столбцов матрицы

    a = numpy.random.randint(-9, 10, (n, m))     # Заполнение матрицы случайными числами

    # Запись матрицы в файл
    file_source = open(path_source, "w")         # Открытие файла на запись
    for i in range(n):
        for j in range(m):
            write_value_file(file_source, a[i][j])       # Запись элемента массива в файл
        file_source.write('\n')

    file_source.close()     # Закрытие файла

    # Чтение матрицы из файла
    file = open(path_source, "r")       # Открытие файла на чтение
    download_matrix = []                # Контейнер прочитанной матрицы

    for string in file:                 # Построчное чтение из матрицы
        row = list(map(int, string.split()))
        download_matrix.append(row)

    file.close()

    # Запись матрицы и обработки
    file_processing_source = open(path_processing_source, "w")  # Открытие файла на запись
    for i in range(n):
        for j in range(m):
            write_value_file(file_processing_source, download_matrix[i][j])
        file_processing_source.write("| " +
            str(count_negative_value_row(download_matrix, i, m)) + "\n")

    # Запись количества отрицательных чисел в строке
    for j in range(m):
        file_processing_source.write("---")

    file_processing_source.write("\n")

    # Запись количества отрицательных чисел в столбце
    for j in range(m):
        file_processing_source.write(" " +
            str(count_negative_value_column(download_matrix, j, n)) + " ")

    file_processing_source.close()