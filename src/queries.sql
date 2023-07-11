DROP DATABASE IF EXISTS %s;
CREATE DATABASE %s;

CREATE TABLE employers (
    company_id int PRIMARY KEY,
    company_name varchar(200),
    url text
    );

CREATE TABLE vacancies (vacancy_id int PRIMARY KEY,
    vacancy varchar(200),
    company_id int,
    salary int,
    url text,

    CONSTRAINT fk_vacancies_employers FOREIGN KEY(company_id) REFERENCES employers(company_id));

INSERT INTO employers VALUES (%s, %s, %s);

SELECT * FROM employers;

INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s);

SELECT company_name, COUNT(vacancy) AS number_of_vacancies
FROM vacancies
INNER JOIN employers USING(company_id)
GROUP BY company_name;

SELECT vacancy, company_name, salary, vacancies.url
FROM vacancies
INNER JOIN employers USING(company_id);

SELECT AVG(salary)
FROM vacancies;

SELECT vacancy, salary, company_name
FROM vacancies
INNER JOIN employers USING(company_id)
WHERE salary > (SELECT AVG(salary) FROM vacancies);

SELECT vacancy
FROM vacancies
WHERE vacancy LIKE %s;