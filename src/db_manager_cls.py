import psycopg2


class DBManager:
    """Класс для работы с данными в БД"""

    def __init__(self, database, params):
        self.conn = psycopg2.connect(dbname=database, **params)

    def truncate_tables(self):
        """Удаляет содержимое таблиц employers, vacancies"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('TRUNCATE TABLE vacancies, employers')

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
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT company_name, COUNT(vacancy) AS number_of_vacancies '
                            'FROM vacancies '
                            'INNER JOIN employers USING(company_id) '
                            'GROUP BY company_name')
                data = cur.fetchall()
                return data

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT vacancy, company_name, salary, vacancies.url '
                            'FROM vacancies '
                            'INNER JOIN employers USING(company_id)')
                data = cur.fetchall()
                return data

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT AVG(salary) '
                            'FROM vacancies')
                data = cur.fetchall()
                return data

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT vacancy, salary, company_name '
                            'FROM vacancies '
                            'INNER JOIN employers USING(company_id) '
                            'WHERE salary > (SELECT AVG(salary) FROM vacancies)')
                data = cur.fetchall()
                return data

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова”"""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f'SELECT vacancy '
                            'FROM vacancies '
                            f'WHERE vacancy LIKE \'%{keyword}%\'')
                data = cur.fetchall()
                return data

    def close_connection(self):
        """Закрывает подключение к БД"""
        self.conn.close()
