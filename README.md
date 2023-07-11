# Employers_parser
___
## Description
The project is intended for parsing and sorting available vacancies of selected companies.
___
## Requirements
- `requests`
- `psycopg2`
___
## DataBase connection
Create a `database.ini` configuration file with your database connection settings.

File content example:
```ini
[postgresql]
host=localhost
user=postgres
password=12345
port=5432
```
___
## Running
By default, there are 10 companies to work with, that can be replaced in the `main.py` file. After running the `main.py` file, for each company all currently available vacancies, posted on the HeadHunter, will be received. The received data is loaded into the database.

The database contains two tables: employers (with the fields: company_id, company_name, url (link to the employer page on the headhunter)) and vacancies (with fields: vacancy_id, vacancy_name, company_id, salary, url(link to the vacancy page on HeadHunter)).

There are 5 functions for working with data:
- `get_companies_and_vacancies_count()`: Gets a list of all companies and the number of vacancies for each company.
- `get_all_vacancies()`: Gets a list of all vacancies with company name, vacancy name and salary, and a link to the vacancy.
- `get_avg_salary()`: Gets the average salary for jobs.
- `get_vacancies_with_higher_salary()`: Gets a list of all vacancies that have an above-average salary.
- `get_vacancies_with_keyword()`: Gets a list of all vacancies whose title contains the words passed to the method (by default, “developer”).

Functions run automatically in the `main.py` file.