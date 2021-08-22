"""Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
комментарий. Реализовать CRUD(создание, чтение, обновление по id, удаление
по id) для продуктов. Создать пользовательский интерфейс."""


# from task_14_1 import *

def create_tuple():
    product_info = []
    product_id = int(input('id: '))
    product_name = input('Название: ')
    product_price = float(input('Цена: '))
    product_quantity = int(input('Количество: '))
    product_comment = input('Комментарий: ')
    tuple_product = (product_id, product_name, product_price, product_quantity, product_comment)
    product_info.append(tuple_product)
    return product_info



