
    # 1) Создать переменную типа String
nameString = 'String'
    # 2) Создать переменную типа Integer
nameInteger = 12345
    # 3) Создать переменную типа Float
nameFloat = 123.45
    # 4) Создать переменную типа Bytes
nameBytes = bytes(nameInteger)
    # 5) Создать переменную типа List
nameList = [1, 2, 3, 4, 5]
    # 6) Создать переменную типа Tuple
nameTuple = ('Vlas',)
nameTuple2 = tuple(nameList)
    # 7) Создать переменную типа Set
nameSet = {1, 2, 3, 3, 4, 4, 4, 5}
nameSet2 = set(nameTuple2)
    # 8. Создать переменную типа Frozen set
nameFrozenSet = frozenset(nameSet)
    # 9) Создать переменную типа Dict
nameDict = {1:"dog", 2:"cat", 3:"mouse"}

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


