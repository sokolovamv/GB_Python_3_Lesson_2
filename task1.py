# Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def hexadecimal(a: int, b: int) -> str: 
    res = ''
    while a > 0:
        mod_a = a % b
        # для систем счисления выше 10
        if mod_a > 9:
            mod_a = chr(mod_a - 10 + 97)
        else:
            mod_a = str(mod_a)
        res = mod_a + res
        a = a // b
    return res

a: int = int(input('Введите целое число: '))
b: int = int(input('Введите систему счисления: '))
print(f'{a} в {b}-ичной системе = {hexadecimal(a, b)}')
# для проверки
print(bin(a))
print(oct(a))
print(hex(a))

