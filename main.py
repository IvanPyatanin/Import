from def_packages.salary import calculate_salary
from def_packages.people import get_employees
from datetime import date


def inp(res):
    if res.isdigit():
        calculate_salary()
    else:
        get_employees()

print(date.today())



if __name__ == '__main__':
    res = input('Введите что число или "Люди": ')
    inp(res)