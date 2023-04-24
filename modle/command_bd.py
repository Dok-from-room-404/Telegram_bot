



'''
В данном файле находятся команды для базы данных

Команды:
-------
* connect_bd - Позволяет подключится к БД
* maid_bd - Создает базу данных
* get_iser - Возвращает пользователя из БД
* get_histori - Возвращает историю по пользователю
* append_user - Добавляем пользователя
* uppdete_user - Обновляет информацию о пользователе
'''
from sqlite3 import connect, Connection, Cursor
import pickle


def connect_bd(name:str):
    '''Позволяет подключится к БД
        \n* name - имя БД'''
    con = connect(name)
    cur = con.cursor()
    return con, cur


def maid_bd(con:Connection, cur:Cursor):
    '''Создает базу данных
        \n* con - подключение к БД
        \n* cur - курсор БД'''
    cur.execute("""CREATE TABLE users (
                    id      INTEGER PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
                                    
                    user_id INTEGER UNIQUE
                                    NOT NULL,
                                    
                    user    BLOB    NOT NULL);""")
    
    cur.execute("""CREATE TABLE history (
                    id      INTEGER REFERENCES users (id) 
                                    UNIQUE
                                    NOT NULL,
                                    
                    history BLOB);""")
    con.commit()


def get_iser(cur:Cursor, id:int):
    '''Возвращает пользователя из БД или None (в случае отсутствия)
       \n* con - подключение к БД
       \n* cur - курсор БД
       \n* id - id пользователя'''
    res = cur.execute("""select user from users
                            where user_id = {id}""".format(id = id)).fetchone()
    # con.commit()
    if res == None:
        return res
    else:
        return pickle.loads(res[0])


def get_histori(cur:Cursor, id:int):
    '''Возвращает историю по пользователю
       \n* con - подключение к БД
       \n* cur - курсор БД'''
    res = cur.execute('''select history from history
                            where id = (select id from users
                                            where user_id = {id})'''.format(id = id)).fetchone()
    # con.commit()
    return res


def append_user(con:Connection, cur:Cursor, id:int, user):
    '''Добавляем пользователя
       \n* con - подключение к БД
       \n* cur - курсор БД
       \n* user - класс пользователя'''
    cur.execute('''INSERT INTO users (user_id, user)
                    VALUES (?, ?)''', (id, pickle.dumps(user)))#, user = user))
    con.commit()


def uppdete_user(con:Connection, cur:Cursor, id:int, user):
    '''Обновляет информацию о пользователе
       \n* con - подключение к БД
       \n* cur - курсор БД
       \n* id - id пользователя
       \n* user - класс пользователя'''
    cur.execute('''UPDATE users 
                    set user = ?
                        where user_id = ?''', (pickle.dumps(user), id))
    con.commit()