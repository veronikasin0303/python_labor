# Паспорт объекта

# Переменные:
student_name = "Син Вероника Вадимовна"
group_number = "3150801/10102"
project_name = "ЖК Like"
floors = 11
height = 30
is_residential = True
construction_year = 2019

# Вывод
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print("Составитель:", student_name)
print("Группа:", group_number)
print()
print("Объект:", project_name)
print("Этажность:", floors, "этажей")
print("Высота:", height, "м")

if is_residential:
    print("Тип: Жилой")
else:
    print("Тип: Нежилой")

print("Год постройки:", construction_year)

# Комментарий:
# Объект находится в г.Санкт-Петербург, ул.Политехническая, д. 6.
# Выбран ЖК, в котором я жила.