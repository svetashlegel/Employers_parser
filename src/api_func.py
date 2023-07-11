import requests
import json


def get_company_by_name(company_name):
    """Возвращает id компании по ее названию"""
    params = {
        'text': company_name,
        'area': 1
    }
    req = requests.get('https://api.hh.ru/employers', params)
    data = req.content.decode()
    req.close()
    dataj = json.loads(data)
    return dataj['items'][0]


def get_vacancies(employer_id):
    """Получает список вакансий компании"""
    params = {
        'employer_id': employer_id,
        'area': 1
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    dataj = json.loads(data)
    return dataj
