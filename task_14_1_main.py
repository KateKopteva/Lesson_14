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


        insert_product = input('Хотите добавить запись в таблицу? YES/NO ')

        if insert_product == 'YES':
            cur.executemany("INSERT INTO product VALUES(?, ?, ?, ?, ?)", create_tuple())
        else:
            print('Таблица готова')

        cur.execute("SELECT * FROM product")
        for result in cur:
            print(result)

if __name__ == '__main__':
    main()
