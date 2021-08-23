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
            change = input('Хотите изменить данные по id? YES/NO ')

            if change == 'YES':
                new_id = int(input('Введите новое значение id: '))
                change_id_product = input('Введите продукт для которого вносятся изменения: ')
                cur.execute("""UPDATE product SET id = :new_id WHERE product = :change_id_product""",
                            ({'new_id': new_id, 'change_id_product': change_id_product}))

            else:
                delete_id = input('Хотите удалить данные по id? YES/NO ')

                if delete_id == 'YES':
                    delete = int(input('Введите значение id, которое удаляем: '))
                    cur.execute("""DELETE FROM product WHERE id = :delete""", {'delete': delete})
                else:
                    print('Таблица готова')

        cur.execute("SELECT * FROM product")
        for result in cur:
            print(result)


if __name__ == '__main__':
    main()
