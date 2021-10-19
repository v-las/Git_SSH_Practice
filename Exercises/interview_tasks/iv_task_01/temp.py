new_list = [i for i in range(180)]
for n, i in enumerate(new_list):
    if i == 170:
        new_list[n] = 'tick'
print(new_list)

a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
for n, i in enumerate(a):
    if i == 1:
        a[n] = 10
print(a)

head_1 = head_2 = head_3 = []
head_roll_1 = ['forw', 'back', 'left', 'right']
head_roll_2 = ['back', 'left', 'right']
head_roll_3 = ['right', 'left', 'forw']
time = 180
def head_roll_func(roll_list, whole_time, tick):
    full_list = [i for i in range(180)]
    new_list = []
    for n, i in enumerate(full_list):
        if i == whole_time:
            for i in roll_list:
                result = str(whole_time) + i
                new_list.append(result)
                whole_time -= tick
                if not whole_time:
                    break
            full_list[n] = result
    return full_list
print(head_roll_func(head_roll_1, time, 10))
print(head_roll_func(head_roll_2, time, 15))
print(head_roll_func(head_roll_3, time, 20))
