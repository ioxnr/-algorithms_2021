"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib

string = input('Введите строку: ')
a = set()
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        if string[i:j] != string:
            a.add(hashlib.sha256(string[i:j].encode()).hexdigest())

print(f'Количество уникальных подстрок: {len(a)}')
print(a)
