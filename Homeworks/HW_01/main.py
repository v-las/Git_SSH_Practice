nameString = 'String'   # 1) Создать переменную типа String
nameInteger = 12345     # 2) Создать переменную типа Integer
nameFloat = 123.45      # 3) Создать переменную типа Float
nameBytes = bytes(nameInteger)  # 4) Создать переменную типа Bytes
nameList = [1, 2, 3, 4, 5]      # 5) Создать переменную типа List

nameTuple = ('Vlas',)               # 6) Создать переменную типа Tuple
nameTuple2 = tuple(nameList)

nameSet = {1, 2, 3, 3, 4, 4, 4, 5}  # 7) Создать переменную типа Set
nameSet2 = set(nameTuple2)

nameFrozenSet = frozenset(nameSet)          # 8) Создать переменную типа Frozen set
nameDict = {1: "dog", 2: "cat", 3: "mouse"}    # 9) Создать переменную типа Dict

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(nameString, type(nameString))
print(nameInteger, type(nameInteger))
print(nameFloat, type(nameFloat))
print(type(nameBytes), nameBytes)
print(nameList, type(nameList))
print(nameTuple, type(nameTuple))
print(nameTuple2, type(nameTuple2))
print(nameSet, type(nameSet))
print(nameSet2, type(nameSet2))
print(nameFrozenSet, type(nameFrozenSet))
print(nameDict, type(nameDict))

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
nameFirstString = '12345'
nameSecondString = 'Vlas'
nameSumString = nameFirstString + nameSecondString
print(nameSumString)

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
nameFirstInt = 54321
nameSecondInt = 12345
nameSumInt = nameFirstInt + nameSecondInt
print(nameSumInt)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
nameDivInt = nameFirstInt / nameSecondInt
print(nameDivInt)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
nameMultiInt = nameFirstInt * nameSecondInt
print(nameMultiInt)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
nameFloorDivInt = nameFirstInt // nameSecondInt
print(nameFloorDivInt)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменнх Int. Вывести в консоль.
nameModInt = nameFirstInt % nameSecondInt
print(nameModInt)

# 17) )))))
