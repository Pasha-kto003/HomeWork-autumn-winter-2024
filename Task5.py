def is_palindrome(s):
    sanitized = ''.join(filter(str.isalnum, s)).lower()  # Убирает пробелы и оставляет только буквы и цифры
    return sanitized == sanitized[::-1]

def main():
    input_str = input("Введите вашу строку: ")
    print('Да' if is_palindrome(input_str) else 'Нет')

if __name__ == "__main__":
    main()
