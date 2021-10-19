tick_list_3 = [i for i in range(180)]
head_1_turns = ['r', 'f', 'b', 'l']
head_2_turns = ['r', 'b', 'l']
head_3_turns = ['f', 'r', 'l']

tick_list_1 = [i for i in range(180)]
for tick in tick_list_1:
    if tick_list_1[tick] // 10 == tick_list_1[tick] / 10:
        head_1_turns.append(head_1_turns.pop(0))
    tick_list_1[tick] = str(tick_list_1[tick]) + head_1_turns[0]
print(tick_list_1)

tick_list_2 = [i for i in range(180)]
for tick in tick_list_2:
    if tick_list_2[tick] // 15 == tick_list_2[tick] / 15:
        head_2_turns.append(head_2_turns.pop(0))
    tick_list_2[tick] = str(tick_list_2[tick]) + head_2_turns[0]
print(tick_list_2)

tick_list_3 = [i for i in range(180)]
for tick in tick_list_3:
    if tick_list_3[tick] // 20 == tick_list_3[tick] / 20:
        head_3_turns.append(head_3_turns.pop(0))
    tick_list_3[tick] = str(tick_list_3[tick]) + head_3_turns[0]
print(tick_list_3)

new_list = []
for i in tick_list_1:
    i = int(i.translate({ord(i): None for i in 'frlb'}))
    # print(i, type(i))
    if tick_list_1[i] == tick_list_2[i] == tick_list_3[i]:
        new_list.append(i)
print(len(new_list))
