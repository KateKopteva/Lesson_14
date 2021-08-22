"""Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
комментарий. Реализовать CRUD(создание, чтение, обновление по id, удаление
по id) для продуктов. Создать пользовательский интерфейс."""
import sqlite3
from task_14_1_input import *


def main():
    with sqlite3.connect("/home/ekaterina/Рабочий стол/opt/omnidb-app/product_DB") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS product(
        id INTEGER,
        product VARCHAR,
        price FLOAT,
        quantity INTEGER,
        comment VARCHAR
        )""")

        cur.executemany("INSERT INTO product VALUES(?, ?, ?, ?, ?)", create_tuple())

        # change = input('Хотите изменить данные? YES/NO ')
        # if change == 'YES':
        #     cur.execute("""UPDATE product SET id = id, product = product, price = price,
        #     quantity = quantity, comment = comment WHERE """)


if __name__ == '__main__':
    main()
