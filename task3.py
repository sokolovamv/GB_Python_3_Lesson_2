# Напишите программу банкомат. 
# Начальная сумма равна 0. 
# Допустимые действия: пополнить, снять, выйти. 
# Сумма пополнения и снятия кратны 50 у.е. 
# Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счете. 
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Вывод меню выбора
def show_menu():
    print('\n' + '=' * 20)
    print("\nВыберите необходимое действие: \n"
    "1. Пополнить счет\n"
    "2. Снять деньги\n"
    "3. Выйти\n")
    return int(input('Введите номер необходимого действия: '))

# Снятие денег
def withdrawal(balance, cash, number_of_operation):
    # проверка на кратность 50 по условию
    if cash % 50 == 0:
        # вычет комиссии за снятие с учетом баланса на счете 
        # номер удачной операции снятия и пополнения
        if 30 <= cash * 0.015 <= 600 and cash * 1.015 < balance:
            balance -= cash * 1.015
            number_of_operation += 1
            print(f'Номер удачной операции: {number_of_operation}')
        elif cash * 0.015 < 30 and cash + 30 < balance:
            balance -= cash + 30
            number_of_operation += 1
            print(f'Номер удачной операции: {number_of_operation}')
        elif cash * 0.015 > 600 and cash + 600 < balance:
            balance -= cash + 600
            number_of_operation += 1
            print(f'Номер удачной операции: {number_of_operation}')
        else:
            print('На балансе не хватает денег')
    else:
        print('Нельзя снять данное количество денег')
    return balance, number_of_operation

# пополнение денег
def refill(cash, number_of_operation):
    # проверка на кратность 50 и подсчет удачных попыток снятия и пополнения
    if cash % 50 == 0:
        number_of_operation += 1
        print(f'Номер удачной операции: {number_of_operation}')
        return cash, number_of_operation
    else:
        print('Нельзя пополнить на данное количество денег')
        return 0, number_of_operation
    
# Кэшбэк после 3 операции
def cashback(balance, per_cashback):
    balance *= (1 + per_cashback / 100)
    return balance

# налог на богатство 
def wealth_tax(balance, tax):
    balance *= (1 - tax / 100)
    return balance

operation = 0   # Количество операций
user_cash = 0   # Баланс на счетее
percent_of_cashback = 3   # процент кэшбэка
rich_account = 5_000_000   # Богатый счет
wealth_tax_percent = 10   # налог на богатство

menu_item = show_menu()   # Вывод меню

while True:
    # проверка на богатство переж каждой операцией
    if user_cash > rich_account:
        user_cash = wealth_tax(user_cash, wealth_tax_percent)
        print(f'Ваш баланс после вычета налога на богатство: {user_cash}')
    
    # пополнение денеег
    if menu_item == 1:
        refill_cash = refill(int(input('Введите сумму для пополнения: ')), operation)
        user_cash += refill_cash[0]
        operation = refill_cash[1]
        print(f'Ваш баланс: {user_cash}')
        # проверка на кэшбэк (не определена ситуация, когда после 3 попытки идет неудачная операция)
        if operation % 3 == 0:
            user_cash = cashback(user_cash, percent_of_cashback)
            print(f'Ваш баланс + кэшбэк после 3 операции: {user_cash}')
        menu_item = show_menu()

    # снятиее денег
    elif menu_item == 2:
        withdrawal_cash = withdrawal(user_cash, int(input('Введите сумму для снятия: ')), operation)
        user_cash = withdrawal_cash[0]
        operation = withdrawal_cash[1]
        print(f'Ваш баланс: {user_cash}')
        if operation % 3 == 0:
            user_cash = cashback(user_cash, percent_of_cashback)
            print(f'Ваш баланс + кэшбэк после 3 операции: {user_cash}')
        menu_item = show_menu()

    # Выход
    elif menu_item == 3:
        print('До скорых встреч!')
        break
    else: 
        print('Такого числа нет в меню. До скорых встреч.')
        break
    
    

