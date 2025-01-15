def palindrom(s):
    palind_row = ''.join(s.split()).lower()
    return palind_row == palind_row[::-1]


def main():
    input_row = input("Введите вашу строку: ")
    if palindrom(input_row):
        print('Данное слово является палиндромом')
    else:
        print('Данное слово не является палиндромом')


if __name__ == "__main__":
    main()