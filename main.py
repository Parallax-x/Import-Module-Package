from application.db.people import get_employees
from application.salary import calculate_salary
import time
from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(3)):
        time.sleep(0.5)
        print(f'\nТекущая дата и время: {time.ctime(time.time())}')
        get_employees()
        calculate_salary()
