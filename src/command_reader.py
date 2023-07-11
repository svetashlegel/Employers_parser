import os


def read_commands_from_file(filename):
    """Получает из файла список sql-запросов"""
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, filename)
    fd = open(initfile, 'r')
    sql_file = fd.read()
    fd.close()
    sql_commands = sql_file.split(';')
    return sql_commands
