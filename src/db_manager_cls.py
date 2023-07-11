import psycopg2


class DBManager:
    """Класс для работы с данными в БД"""

    def __init__(self, database, params, sql_commands):
        self.conn = psycopg2.connect(dbname=database, **params)
        self.sql_commands = sql_commands

    def create_tables(self):
        """Создает таблицы employers и vacancies в БД"""
        for command in self.sql_commands[2:4]:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(command)

    def save_employer(self, company_id, company_name, url):
        """Сохраняет данные по работодателю в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[4], (company_id, company_name, url))

    def get_employers(self):
        """Получает список всех компаний из таблицы employers в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[5])
                data = cur.fetchall()
                return data

    def save_vacancy(self, vacancy_id, vacancy, company_id, salary, url):
        """Сохраняет данные по вакансии в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[6], (vacancy_id, vacancy, company_id, salary, url))

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[7])
                data = cur.fetchall()
                return data

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[8])
                data = cur.fetchall()
                return data

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[9])
                data = cur.fetchall()
                return data

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[10])
                data = cur.fetchall()
                return data

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова”"""
        keystring = f'\'%{keyword}%\''
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(self.sql_commands[11] % keystring)
                data = cur.fetchall()
                return data

    def close_connection(self):
        """Закрывает подключение к БД"""
        self.conn.close()
