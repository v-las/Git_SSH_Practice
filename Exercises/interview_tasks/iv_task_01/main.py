def tick_count(turns, time):
    """
    Создаётся и итерируется список минут в трёх часах.
    К каждой минуте добавляется направление головы.
    При каждом времени поворота в списке направлений первый элемент
    перемещается в конец, чтобы добавлялся следующий.
    :param turns: Список направлений головы.
    :param time: Время поворота.
    :return: Список минут с направлением головы в каждую минуту.
    """
    ticks = [i for i in range(180)]
    for i in ticks:
        if ticks[i] // time == ticks[i] / time:
            turns.append(turns.pop(0))
        ticks[i] = str(ticks[i]) + turns[0]
    return ticks

# Время поворота каждой головы
head_1_time = 10
head_2_time = 15
head_3_time = 20
# Сторона направления головы
head_1_turns = ['r', 'f', 'b', 'l']
head_2_turns = ['r', 'b', 'l']
head_3_turns = ['f', 'r', 'l']
# Время и стороны отправляются в функцию
head_1_workout = tick_count(head_1_turns, head_1_time)
head_2_workout = tick_count(head_2_turns, head_2_time)
head_3_workout = tick_count(head_3_turns, head_3_time)
# Итерируется список для поиска совпадений
minute_list = []
for i in head_1_workout:
    # Очищается список от букв, приводится к int, чтобы получить список индексов
    i = int(i.translate({ord(i): None for i in 'fblr'}))
    # Сравниваются между собой списки трёх голов
    if head_1_workout[i] == head_2_workout[i] == head_3_workout[i]:
        # Совпадения (минуты с одинаковым направлением) добавляются в лист
        minute_list.append(i)
# Вывод в консоль подсчитанных элементов листа (минут)
print("Три головы смотрели в одну сторону", len(minute_list), "минут.")
