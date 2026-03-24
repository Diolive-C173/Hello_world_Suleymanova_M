#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

# Создание и запись файла в формате таблицы
with open('sensor_log.txt', 'w', encoding='utf-8') as file:
    file.write("ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write("-" * 30 + "\n")
    file.write(f"{operator_name}\t{pressure_value}")

print("\nДанные успешно сохранены в sensor_log.txt")