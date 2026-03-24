#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
protein = float(input("Введите массу белков (г): "))
fat = float(input("Введите массу жиров (г): "))
carbohydrates = float(input("Введите массу углеводов (г): "))

# Расчет общей калорийности
calories = (protein * 4) + (fat * 9) + (carbohydrates * 4)

# Вывод результата с использованием f-строки
print(f"\nОбщая калорийность продукта: {calories:.2f} ккал")
