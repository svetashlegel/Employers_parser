def print_companies_and_vacancies_count(data):
    """Преобразует и выводит на экран информацию по кол-ву вакансий в компании"""
    for i in data:
        if i[1] == 1:
            vac = 'вакансия'
        elif i[1] in [2, 2, 4]:
            vac = 'вакансии'
        else:
            vac = 'вакансий'
        print(f"{i[0]} - {i[1]} {vac}")


def print_all_vacancies(data):
    """Преобразует и выводит на экран информацию по каждой вакансии"""
    for i in data:
        print(f"Должность: {i[0]}\n"
              f"Компания: {i[1]}\n"
              f"Зарплата: {i[2]}\n"
              f"Ссылка на вакансию: {i[3]}\n")


def print_avg_salary(data):
    """Преобразует и выводит на экран среднюю зарплату"""
    print(f"Средняя зарплата по вакансиям: {round(data[0][0])}")


def print_vacancies_with_higher_salary(data):
    """Преобразует и выводит на экран вакансии с уровнем зарплаты выше среднего"""
    print("Вакансии, с уровнем зарплаты выше среднего:")
    for i in data:
        print(f"{i[0]} ({i[2]}): {i[1]} руб.")


def print_vacancies_with_keyword(data):
    """Преобразует и выводит на экран вакансии по ключевому слову"""
    print(f"Вакансии по ключевому слову:")
    for i in data:
        print(i[0])
