# Lesson 2

b_true = True
b_false = False

v_1 = 3
v_2 = 3
print(v_1 == v_2)   # Равно
print(v_1 != v_2)   # Неравно
print(v_1 > v_2)
print(v_1 < v_2)
print(v_1 >= v_2)
print(v_1 <= v_2)

age = 32
weight = 97
qa = True

result = age > 30 and weight > 90   # and
print(result)
result = age == 32 and weight > 90
print(result)

result = age > 30 or weight > 90   # or
print(result)
result = age == 32 or weight > 90
print(result)

result = not age == 35   # not
print(result)

if age == 32:
    print('Condition_1')
    if weight == 97:
        print('Condition_4')
    else:
        print('Condition_5')
elif age > 35:
    print('Condition_3')
else:
    print('Condition_2')
