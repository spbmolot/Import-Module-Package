from datetime import date

from application.db.people import get_employees
from application.salary import calculate_salary



if __name__ == '__main__':
    print(date.today())
    get_employees()
    calculate_salary()


