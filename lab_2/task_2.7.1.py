#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Фиксированная дата взятия образца
sample_date = "2024-03-15"

# Список названий образцов
samples = ["sample1", "sample2", "control", "test", "blank"]

print("Генерация названий файлов:")
print("-" * 40)

# Генерация названий файлов с датой
for sample in samples:
    filename = f"{sample}_{sample_date}.fasta"
    print(filename)

