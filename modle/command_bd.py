



'''
В данном файле находятся команды для базы данных

Команды:
-------
* get_iser - Возвращает пользователя из БД
* maid_bd - Создает базу данных
'''
import sqlite3


def connect_bd(name:str):
    '''Позволяет подключится к БД
    *name - имя БД'''
    con = sqlite3.connect(name)
    cur = con.cursor()
    return con, cur


def get_iser(con, cur, id):
    '''Возвращает пользователя из БД
       *con - подключение к БД
       *cur - курсор БД
       *id - id пользователя'''
    res = cur.execute("""select user from users
                    where user_id = {id}""".format(id = id)).fetchone()
    con.commit()
    return res


def maid_bd():
    '''Создает базу данных'''


def get_histori():
    '''Возвращает историю по пользователю'''
    '''select * from history
    where id = (select id from users
                    where user_id = 56)'''