#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Запрос данных у пользователя
total_capsules = int(input("Введите общее количество произведенных капсул: "))
packaging_capacity = int(input("Введите количество капсул в одной упаковке: "))

# Расчет количества полных упаковок и остатка
full_packages = total_capsules // packaging_capacity
remaining_capsules = total_capsules % packaging_capacity

# Вывод отчета
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t\t{remaining_capsules}")