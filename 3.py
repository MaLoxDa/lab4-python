# Задание3

print("Составление расписания звонков на учебный день")

start_h = int(input("Час начала занятий (например, 8): "))
start_m = int(input("Минуты начала занятий (например, 0): "))
lesson = int(input("Продолжительность пары/урока в минутах (например, 45): "))
small_break = int(input("Продолжительность обычного перерыва (например, 10): "))
big_break = int(input("Продолжительность большого перерыва (например, 20): "))
big_after = int(input("После какой пары/урока большой перерыв (например, 2): "))
count = int(input("Сколько всего пар/уроков (например, 4): "))

time = start_h * 60 + start_m   
i = 1

while i <= count:
    h1 = time // 60
    m1 = time % 60

    end = time + lesson
    h2 = end // 60
    m2 = end % 60

    print(f"Пара/урок {i}: {h1:02d}:{m1:02d} - {h2:02d}:{m2:02d}")

    # последняя пара/урок
    time = end

    if i == count:
        i = i + 1
    else:
        if i == big_after:
            time = time + big_break
        else:
            time = time + small_break
        i = i + 1

print("Конец учебного дня")