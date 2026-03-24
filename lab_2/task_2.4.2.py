#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))

# Перевод роста из сантиметров в метры
height_m = height_cm / 100

# Расчет индекса массы тела (ИМТ)
bmi = weight / (height_m ** 2)

# Вывод отчета с использованием управляющих символов
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t\t{height_cm:.1f} см")
print(f"Вес:\t\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")