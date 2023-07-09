import psycopg2


class DBManager:
    """Класс для работы с данными в БД"""

    def __init__(self, database):
        self.conn = psycopg2.connect(
            host='localhost',
            database=database,
            user='postgres',
            password='1651'
        )

    def save_employer(self, company_id, company_name, url):
        """Сохраняет данные по работодателю в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('INSERT INTO employers VALUES (%s, %s, %s)', (company_id, company_name, url))

    def get_employers(self):
        """Получает список всех компаний из таблицы employers в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT * FROM employers')
                data = cur.fetchall()
                return data

    def save_vacancy(self, vacancy_id, vacancy, company_id, salary, url):
        """Сохраняет данные по вакансии в БД"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)',
                            (vacancy_id, vacancy, company_id, salary, url))

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        pass

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней"""
        pass

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова”"""
        pass

    def close_connection(self):
        """Закрывает подключение к БД"""
        self.conn.close()
