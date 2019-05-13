import json

symbols = ['`', '~', '!', '@', '#', '№', '$', '%', '^', ':', '&', '?', '*', '(', ')', '-', '_', '=', '+', '1', '2', '3',
           '4', '5', '6', '7', '8', '9', '0', '/', '.', ',', '\\', '|', ';', 'q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't',
           'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', '{', '[', '}', ']', 'a', 'A', 's', 'S', 'd', 'D', 'f',
           'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b',
           'B', 'n', 'N', 'm', 'M', '<', '>']

passwords = []

filename = input('Введите имя файла: ')
pass_length = int(input('Введите длину пароля: '))

def pass_gen(pass_length:int, prefix=''):
    """
    Генерирует словарь паролей заданной длины M
    """
    if pass_length == 0:
        passwords.append(prefix)
        print(prefix)
        return
    for symbol in symbols:
        pass_gen(pass_length-1, prefix+symbol)
    with open(filename + '.json', 'w', encoding='utf-8') as file:
        json.dump(passwords, file, ensure_ascii=False, indent=2)

pass_gen(pass_length)

