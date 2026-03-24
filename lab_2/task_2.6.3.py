#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввод фенотипа с очисткой от пробелов и приведением к верхнему регистру
phenotype = input("Введите фенотип группы крови (I, II, III, IV): ").strip().upper()

# Определение группы крови
if phenotype == "I" or phenotype == "1" or phenotype == "ПЕРВАЯ" or phenotype == "FIRST":
    print("Группа крови: 0 (I)")
elif phenotype == "II" or phenotype == "2" or phenotype == "ВТОРАЯ" or phenotype == "SECOND":
    print("Группа крови: A (II)")
elif phenotype == "III" or phenotype == "3" or phenotype == "ТРЕТЬЯ" or phenotype == "THIRD":
    print("Группа крови: B (III)")
elif phenotype == "IV" or phenotype == "4" or phenotype == "ЧЕТВЕРТАЯ" or phenotype == "FOURTH":
    print("Группа крови: AB (IV)")
else:
    print("Такой группы крови не существует")

