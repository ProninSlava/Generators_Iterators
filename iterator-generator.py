# ИТЕРАТОРЫ

class Iter_den():

    def __init__(self, n=5):
        self.n = n

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.n:
            raise "Итерация закончилась"
        return 'hello'

# iter_gen = Iter_den()
#
# for item in iter_gen:
#     print(item)

class MyRange:

    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.cursor = self.start - self.step
        return self

    def __next__(self):
        self.cursor += self.step
        if self.cursor >= self.end:
            raise 'Итерация закончилась'

        return self.cursor

# ran = MyRange(1,6)
#
# for item in ran:
#     print(item)


# ГЕНЕРАТОР

def gener(start: int, end: int):
    list_iter = []
    while end > start:
        start += 1
        list_iter.append(start)
    return list_iter

# print(gener(1, 6))
#
# for item in gener(1, 6):
#     print(item)

def gener_(start: int, end: int):

    while end > start:
        yield start
        start += 1

for item in gener_(1, 6):
    print(item)

# Функции которые используют yield это генераторы!!!