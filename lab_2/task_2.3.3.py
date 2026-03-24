#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Сбор данных от пользователя
researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# Создание файла с красивой рамкой
with open('journal.txt', 'w', encoding='utf-8') as file:
    # Верхняя граница
    file.write("+" + "-" * 50 + "+\n")
    file.write("|" + " " * 15 + "Электронный лабораторный журнал" + " " * 15 + "|\n")
    file.write("+" + "-" * 50 + "+\n")

    # Основная информация
    file.write(f"| ФИО исследователя : {researcher_name:<32}|\n")
    file.write(f"| Дата              : {date:<42}|\n")
    file.write(f"| Эксперимент       : {experiment_name:<38}|\n")
    file.write("+" + "-" * 50 + "+\n")

    # Вывод с переносом строк
    file.write("| Вывод:                                           |\n")

    # Форматирование вывода с переносом строк (максимум 48 символов в строке)
    max_width = 48
    words = conclusion.split()
    line = ""

    for word in words:
        if len(line) + len(word) + 1 <= max_width:
            if line:
                line += " " + word
            else:
                line = word
        else:
            file.write(f"| {line:<48}|\n")
            line = word

    # Последняя строка вывода
    if line:
        file.write(f"| {line:<48}|\n")

    # Нижняя граница
    file.write("+" + "-" * 50 + "+\n")

print("\nЖурнал успешно сохранен в файл journal.txt")