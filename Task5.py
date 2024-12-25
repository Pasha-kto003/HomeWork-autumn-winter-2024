def palindrom(s):
    palind_row = ''.join(s.split()).lower()
    return palind_row == palind_row[::-1]


def main():
    input_row = input("Введите вашу строку: ")
    if palindrom(input_row):
        print('Да')
    else:
        print('Нет') #//


if __name__ == "__main__":
    main()