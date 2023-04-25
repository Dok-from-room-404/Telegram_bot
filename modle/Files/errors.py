"""
Данный модуль содержит исключения для работы бота с файлами

Исключения:
----------
    * NET_ERROR - Класс ошибки. Возникает при добавление недопустимой соц. сети
    * LINK_ERROR - Класс ошибки. Возникает при добавление недопустимой ссылки
"""



class NET_ERROR(Exception):
    """Класс ошибки. Возникает при добавление недопустимой соц. сети"""
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        if self.inform:
            return 'NET_ERROR: {0} '.format(self.inform)
        else:
            return 'NET_ERROR'


class LINK_ERROR(Exception):
    """Класс ошибки. Возникает при добавление недопустимой ссылки"""
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        if self.inform:
            return 'LINK_ERROR: {0} '.format(self.inform)
        else:
            return 'LINK_ERROR'


class FORMAT_ERROR(Exception):
    """Класс ошибки. Возникает при выборе недопустимый формат файла"""
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        if self.inform:
            return 'FORMAT_ERROR: {0} '.format(self.inform)
        else:
            return 'FORMAT_ERROR'


class TYPE_ERROR(Exception):
    """Класс ошибки. Возникает при выборе недопустимый тип файла"""
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        if self.inform:
            return 'TYPE_ERROR: {0} '.format(self.inform)
        else:
            return 'TYPE_ERROR'
