from src.api_func import get_company_by_name, get_vacancies
from src.config import config
from src.command_reader import read_commands_from_file
from src.db_creator import create_database
from src.db_manager_cls import DBManager
from src.print_funcs import print_companies_and_vacancies_count, print_all_vacancies, print_avg_salary, \
    print_vacancies_with_higher_salary, print_vacancies_with_keyword


database = 'comp_vacancies'
sql_file = 'queries.sql'
params = config()
companies = ['Альфа-Банк', 'Тинькофф',  'Сбер IT', 'Ростелеком', 'HR Prime', 'Mindbox', 'Tevian', 'Digital Reputation',
             'Anabar', 'Rubbles']
keyword_for_search = 'разработчик'


sql_commands = read_commands_from_file(sql_file)
create_database(database, params, sql_commands)
db_manager = DBManager(database, params, sql_commands)
db_manager.create_tables()

for company in companies:
    comp_data = get_company_by_name(company)
    db_manager.save_employer(comp_data['id'], comp_data['name'], comp_data['alternate_url'])

emp_data = db_manager.get_employers()
for emp in emp_data:
    vacancies = get_vacancies(emp[0])
    for vac in vacancies['items']:
        if not vac['salary']:
            salary = None
        else:
            if vac['salary']['from'] != 0:
                salary = vac['salary']['from']
            else:
                salary = vac['salary']['to']
        db_manager.save_vacancy(vac['id'], vac['name'], emp[0], salary, vac['alternate_url'])

vacancies_per_company = db_manager.get_companies_and_vacancies_count()
print_companies_and_vacancies_count(vacancies_per_company)
print()
all_vacancies = db_manager.get_all_vacancies()
print_all_vacancies(all_vacancies)
print()
avg_salary = db_manager.get_avg_salary()
print_avg_salary(avg_salary)
print()
vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
print_vacancies_with_higher_salary(vacancies_with_higher_salary)
print()
vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword_for_search)
print_vacancies_with_keyword(vacancies_with_keyword, keyword_for_search)
db_manager.close_connection()
