def tick_count(ticks, turns, time):
    """
    Создаётся и итерируется копия списка минут.
    К каждой минуте добавляется направление головы.
    При каждом времени поворота в списке направлений первый элемент
    перемещается в конец, чтобы добавлялся следующий.
    :param turns: Список направлений головы.
    :param time: Время поворота.
    :return: Список минут с направлением головы в каждую минуту.
    """
    ticks_copy = ticks.copy()
    for i in list(ticks_copy):
        if ticks_copy[i] // time == ticks_copy[i] / time:
            turns.append(turns.pop(0))
        ticks_copy[i] = str(ticks_copy[i]) + turns[0]
    return ticks_copy


# Создаётся список минут в трёх часах
head_ticks = [i for i in range(180)]
# Для каждой головы: время поворота и направления отправляются в функцию
head_1_workout = tick_count(head_ticks, ['r', 'f', 'b', 'l'], 10)
head_2_workout = tick_count(head_ticks, ['r', 'b', 'l'], 15)
head_3_workout = tick_count(head_ticks, ['f', 'r', 'l'], 20)
# Итерируется список для поиска совпадений
minute_list = []
for i in head_ticks:
    # Сравниваются между собой списки трёх голов
    if head_1_workout[i] == head_2_workout[i] == head_3_workout[i]:
        # Совпадения (минуты с одинаковым направлением) добавляются в лист
        minute_list.append(i)
# Вывод в консоль подсчитанных элементов листа (минут)
print("Три головы смотрели в одну сторону", len(minute_list), "минут.")
