def tick_count(turns, time):
    ticks = [i for i in range(180)]
    for i in ticks:
        if ticks[i] // time == ticks[i] / time:
            turns.append(turns.pop(0))
        ticks[i] = str(ticks[i]) + turns[0]
    return ticks


head_1_time = 10
head_2_time = 15
head_3_time = 20
head_1_turns = ['r', 'f', 'b', 'l']
head_2_turns = ['r', 'b', 'l']
head_3_turns = ['f', 'r', 'l']
head_1_workout = tick_count(head_1_turns, head_1_time)
head_2_workout = tick_count(head_2_turns, head_2_time)
head_3_workout = tick_count(head_3_turns, head_3_time)
new_list = []
for i in head_1_workout:
    i = int(i.translate({ord(i): None for i in 'fblr'}))
    if head_1_workout[i] == head_2_workout[i] == head_3_workout[i]:
        new_list.append(i)
print("Три головы смотрели в одну сторону", len(new_list), "минут.")