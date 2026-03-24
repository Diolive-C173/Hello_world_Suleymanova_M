#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
media_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

# Создание и запись файла
with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(f"{media_name}\n")
    file.write("-" * 40 + "\n\n")
    file.write("Параметры:\n")
    file.write(f"  • Концентрация агара: {agar_concentration}%\n")
    file.write(f"  • Температура стерилизации: {sterilization_temp}°C\n")

print("\nФайл 'recipe.txt' успешно сформирован!")