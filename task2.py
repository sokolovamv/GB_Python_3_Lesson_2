# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import math
import fractions 

# Функция преобразования дроби
def fract_conversation(fract: list) -> str:
    # если при делении образуется целое число
    if fract[0] % fract[1] == 0:
        return str(fract[0] // fract[1])
    # сокращем дробь
    else:
        return f'{int(fract[0] / math.gcd(fract[0],fract[1]))}/{int(fract[1] / math.gcd(fract[0],fract[1]))}'

fraction_1: str = input('Введите дробь_1 вида “a/b”: ')
fraction_2: str = input('Введите дробь_2 вида “a/b”: ')

number_1 = [int(i) for i in fraction_1.split('/')]
number_2 = [int(i) for i in fraction_2.split('/')]

# Наименьшее общее кратное (общий знаменатель)
common_denominator = math.lcm(number_1[1], number_2[1])

# Новые числители
numerator_1 = common_denominator / number_1[1] * number_1[0]
numerator_2 = common_denominator / number_2[1] * number_2[0]

# Сумма дробей: список: 1 число - числитель, 2 число - знаменатель
sum_fract = [int(numerator_1 + numerator_2), common_denominator] 

# Произведение дробей: список: 1 число - числитель, 2 число - знаменатель
product_fract = [number_1[0] * number_2[0], number_1[1] * number_2[1]]

# Вывод ответа после преобразования
print('{} + {} = {}'.format(fraction_1, fraction_2, fract_conversation(sum_fract))) 
print('{} * {} = {}'.format(fraction_1, fraction_2, fract_conversation(product_fract))) 

# проверка
f_one = fractions.Fraction(number_1[0], number_1[1]) 
f_two = fractions.Fraction(number_2[0], number_2[1]) 
print('{} + {} = {}'.format(f_one, f_two, f_one + f_two)) 
print('{} * {} = {}'.format(f_one, f_two, f_one * f_two)) 

