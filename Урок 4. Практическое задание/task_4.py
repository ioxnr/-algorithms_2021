"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    number = max(array, key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f'Время выполнения func_1: {timeit("func_1()", globals=globals())}')
print(f'Время выполнения func_2: {timeit("func_2()", globals=globals())}')
print(f'Время выполнения func_3: {timeit("func_3()", globals=globals())}')

'''
Время выполнения func_1: 1.400135699
Время выполнения func_2: 1.814353575
Время выполнения func_3: 1.2969258110000004
Выводы:
1) в функции func_1 в две переменные с помощью цикла вычислялись и записывались наиболее часто встречающееся число 
и количество его появлений в массиве, в цикле каждый раз находилось количество вхождений очередного числа, даже если
такое значение уже вычислялось для него;
2) функция func_2 медленнее, чем func_2 и в ней создается новый массив путем перебора через цикл значений исходного 
массива и записи количеств нахождений этих чисел. Самая медленная она потому, что при каждом выборе нового элемента в 
массиве, функция пробегает по исходному массиву, считая количество вхождений числа; 
3) функция func_3 самая оптимальная и использует встроенную функцию max и метод списка .count();
4) финальный итог: самая быстрая функция - func_3, где нет необходимости каждый раз в цикле пробегать по массиву, 
считая количество вхождений числа.
'''
