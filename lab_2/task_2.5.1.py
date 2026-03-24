#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=== Анализ последовательности ДНК ===\n")

# Получаем последовательность от пользователя
dna_input = input("Введите последовательность ДНК: ")

# Приводим к верхнему регистру
dna_upper = dna_input.upper()

# Выводим последовательность в верхнем регистре
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")

# Подсчет нуклеотидов
nucleotides = ['A', 'T', 'G', 'C']
counts = {}

for nucleotide in nucleotides:
    counts[nucleotide] = dna_upper.count(nucleotide)

# Вывод подсчета нуклеотидов
print("\nПодсчёт нуклеотидов:")
for nucleotide in nucleotides:
    print(f"{nucleotide}: {counts[nucleotide]}")

# Вывод общей длины
length = len(dna_upper)
print(f"\nОбщая длина: {length} нуклеотидов")

# Расчет и вывод процентного содержания
print("\nПроцентное содержание:")
for nucleotide in nucleotides:
    if length > 0:
        percentage = (counts[nucleotide] / length) * 100
    else:
        percentage = 0
print(f"{nucleotide}: {percentage:.2f}%")