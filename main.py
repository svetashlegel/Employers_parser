from src.api_func import get_company_by_name, get_vacancies
from src.db_manager_cls import DBManager

companies = ['Альфа-Банк', 'Тинькофф',  'Сбер IT', 'Ростелеком', 'HR Prime', 'Mindbox', 'Tevian', 'Digital Reputation',
             'Anabar', 'Rubbles']
database = 'comp_vacancies'

db_manager = DBManager(database)
db_manager.truncate_tables()
for company in companies:
    comp_data = get_company_by_name(company)
    url = f"https://hh.ru/employer/{comp_data['id']}"
    db_manager.save_employer(comp_data['id'], comp_data['name'], url)

emp_data = db_manager.get_employers()
for emp in emp_data:
    vacancies = get_vacancies(emp[0])
    for vac in vacancies['items']:
        url = f"https://hh.ru/vacancy/{vac['id']}"
        if not vac['salary']:
            salary = None
        else:
            if vac['salary']['from'] != 0:
                salary = vac['salary']['from']
            else:
                salary = vac['salary']['to']
        db_manager.save_vacancy(vac['id'], vac['name'], emp[0], salary, vac['alternate_url'])

db_manager.close_connection()
