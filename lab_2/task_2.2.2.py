#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Инициализация переменных для учета лабораторного оборудования
equipment_name_1 = "Микроскоп"
inventory_number_1 = "INV-00123"
is_functional_1 = "исправен"
quantity_1 = 5

equipment_name_2 = "Центрифуга"
inventory_number_2 = "INV-00456"
is_functional_2 = "исправен"
quantity_2 = 3

equipment_name_3 = "Термостат"
inventory_number_3 = "INV-00789"
is_functional_3 = "неисправен"
quantity_3 = 1

# Вывод заголовка таблицы
print("Название прибора\tИнвентарный номер\tСостояние\tКоличество")
print("-" * 70)

# Вывод данных
print(f"{equipment_name_1}\t\t{inventory_number_1}\t\t{is_functional_1}\t\t{quantity_1}")
print(f"{equipment_name_2}\t\t{inventory_number_2}\t\t{is_functional_2}\t\t{quantity_2}")
print(f"{equipment_name_3}\t\t{inventory_number_3}\t\t{is_functional_3}\t\t{quantity_3}")