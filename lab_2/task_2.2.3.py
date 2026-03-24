#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (шт.): "))

# Формирование отчета
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

# Вывод отчета в консоль
print(report)

# Запись отчета в файл
with open('inventory.txt', 'w', encoding='utf-8') as file:
    file.write(report)

print("\nОтчет сохранен в файл inventory.txt")