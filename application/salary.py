def calculate_salary():
    income = int(input('Сколько часов вы отработали? ')) * 2500
    print('Ваша зарплата в этом месяце', income, 'рублей')

if __name__ == 'main':
    calculate_salary()