from datetime import datetime
from application.salary import calculate_salary
from application.DB.people import get_employees

todays_date = datetime.today().strftime('%d.%m.%y')
print('Сегодняшнее число', todays_date)

class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password


def main():
    user = User('Пользователь', '123456')
    print('Здравствуйте', user.name)
    while True:
        action = input('Введите команду ')
        if action == 's':
            calculate_salary()
        if action == 'p':
            get_employees()
        if action == 'e':
            break

if __name__ == '__main__':
    main()
