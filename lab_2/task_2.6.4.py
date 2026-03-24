#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Принимаем группу крови донора и реципиента
donor_blood = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()

# Определение возможности переливания
# Универсальный донор - I группа (0), может переливаться всем
# Другие группы совместимы только с собой и с I группой (донор может отдавать только своей группе и I группе реципиентов?)

# Правила совместимости:
# I группа (0) - универсальный донор (может переливаться всем)
# II группа (A) - может переливаться II и IV
# III группа (B) - может переливаться III и IV
# IV группа (AB) - может переливаться только IV

if donor_blood == "I" or donor_blood == "1":
    # I группа - универсальный донор
    print(f"\nДонор с группой крови {donor_blood} может переливать кровь реципиенту с группой {recipient_blood}")
    print("✓ Переливание возможно (I группа - универсальный донор)")
elif donor_blood == "II" or donor_blood == "2":
    if recipient_blood == "II" or recipient_blood == "2" or recipient_blood == "IV" or recipient_blood == "4":
        print(f"\nДонор с группой крови {donor_blood} может переливать кровь реципиенту с группой {recipient_blood}")
        print("✓ Переливание возможно (II группа совместима с II и IV)")
    else:
        print(f"\nДонор с группой крови {donor_blood} НЕ может переливать кровь реципиенту с группой {recipient_blood}")
        print("✗ Переливание невозможно (II группа совместима только с II и IV)")
elif donor_blood == "III" or donor_blood == "3":
    if recipient_blood == "III" or recipient_blood == "3" or recipient_blood == "IV" or recipient_blood == "4":
        print(f"\nДонор с группой крови {donor_blood} может переливать кровь реципиенту с группой {recipient_blood}")
        print("✓ Переливание возможно (III группа совместима с III и IV)")
    else:
        print(f"\nДонор с группой крови {donor_blood} НЕ может переливать кровь реципиенту с группой {recipient_blood}")
        print("✗ Переливание невозможно (III группа совместима только с III и IV)")
elif donor_blood == "IV" or donor_blood == "4":
    if recipient_blood == "IV" or recipient_blood == "4":
        print(f"\nДонор с группой крови {donor_blood} может переливать кровь реципиенту с группой {recipient_blood}")
        print("✓ Переливание возможно (IV группа совместима только с IV)")
    else:
        print(f"\nДонор с группой крови {donor_blood} НЕ может переливать кровь реципиенту с группой {recipient_blood}")
        print("✗ Переливание невозможно (IV группа совместима только с IV)")
else:
print("Ошибка: введена некорректная группа крови")