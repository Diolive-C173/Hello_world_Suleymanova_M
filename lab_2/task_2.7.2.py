#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Список последовательностей
sequences = ["ATATACGCGTA", "CTTCGGNGGA"]

print("Анализ последовательностей ДНК")
print("=" * 60)

# Перебор каждой последовательности
for seq in sequences:
    print(f"\nПоследовательность целиком: {seq}")
    print("Поэлементный вывод:")

    # Поэлементный вывод текущей последовательности
    for letter in seq:
        print(f"  {letter}")

    print("-" * 40)

print("\nЦикл выполнен")




3
