



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


def connect_bd(name:str):
    '''Позволяет подключится к БД
    *name - имя БД'''
    con = connect(name)
    cur = con.cursor()
    return con, cur


def maid_bd(con:Connection, cur:Cursor):
    '''Создает базу данных'''
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


def get_iser(con:Connection, cur:Cursor, id:int):
    '''Возвращает пользователя из БД
       *con - подключение к БД
       *cur - курсор БД
       *id - id пользователя'''
    res = cur.execute("""select user from users
                            where user_id = {id}""".format(id = id)).fetchone()
    con.commit()
    return res


def get_histori(con:Connection, cur:Cursor, id:int):
    '''Возвращает историю по пользователю'''
    res = cur.execute('''select history from history
                            where id = (select id from users
                                            where user_id = {id})'''.format(id = id)).fetchone()
    con.commit()
    return res


def append_user(con:Connection, cur:Cursor, id:int, user):
    '''Добавляем пользователя'''
    cur.execute('''INSERT INTO users (user_id, user)
                    VALUES (?, ?)''', (id, user))#, user = user))
    con.commit()


def uppdete_user(con:Connection, cur:Cursor, id:int, user):
    '''Обновляет информацию о пользователе'''
    cur.execute('''UPDATE users 
                    set user = ?
                        where user_id = ?''', (user, id))
    con.commit()