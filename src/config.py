from configparser import ConfigParser
import os


def config(filename='database.ini', section="postgresql"):
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, filename)
    parser = ConfigParser()
    parser.read(initfile)
    db = {}
    params = parser.items(section)
    for param in params:
        db[param[0]] = param[1]
    return db
