def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").strip().split()))
                if len(row) != cols:
                    raise ValueError("Количество элементов в строке не совпадает с заданным количеством столбцов.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте ещё раз.")
    return matrix


def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def main():
    try:
        rows = int(input("Введите количество строк матрицы (>= 2): "))
        cols = int(input("Введите количество столбцов матрицы (>= 2): "))
        if rows < 2 or cols < 2:
            print("Ошибка: Размеры матрицы должны быть >= 2.")
            return

        print("Введите первую матрицу:")
        matrix1 = read_matrix(rows, cols)

        print("Введите вторую матрицу:")
        matrix2 = read_matrix(rows, cols)

        # Сложение матриц
        result = add_matrices(matrix1, matrix2)

        # Вывод результата
        print("Результат сложения матриц:")
        for row in result:
            print(" ".join(map(str, row)))

    except ValueError:
        print("Ошибка: Введите корректные целые числа.")


if __name__ == "__main__":
    main()
