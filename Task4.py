def read_matrix(rows):
    matrix = []
    for i in range(rows):
        row = input(f"Введите элементы {i + 1}-ой строки через пробел: ").strip().split()
        matrix.append([int(num) for num in row])
    return matrix


def sum_matrix(matrix1, matrix2):
    stroki = len(matrix1)
    stolb = len(matrix1[0])
    result_matrix = []
    for i in range(stroki):
        result_row = []
        for j in range(stolb):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(result_row)
    return result_matrix


def main():
    try:
        stroki = int(input("Введите количество строк матрицы (больше или равно 2): "))
        stolb = int(input("Введите количество столбцов матрицы (больше или равно 2): "))
        if stroki < 2 or stolb < 2:
            print("Ошибка: размер матрицы должен быть больше 2.")
            return
        print("Введите первую матрицу:")
        matrix1 = read_matrix(stroki)
        print("Введите вторую матрицу:")
        matrix2 = read_matrix(stroki)
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Ошибка: Размеры матриц должны совпадать.")
            return
        # Сложение матриц
        result = sum_matrix(matrix1, matrix2)
        print("Результат сложения матриц:")
        for row in result:
            print(" ".join(map(str, row)))
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные целые числа.")


if __name__ == "__main__":
    main()