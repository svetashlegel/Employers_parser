import psycopg2


def create_database(database, params, sql_commands):
    """Создание базы данных для сохранения данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    for command in sql_commands[0:2]:
        cur.execute(command % database)
    conn.close()
