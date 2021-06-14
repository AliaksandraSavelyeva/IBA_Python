# класс объектов, которые одновременно являются и
# итерируемыми (есть метод __iter__),
# и итераторами (есть метод __next__);
class RangeIterableIterator:
    def __init__(self, size):
        self.x = size

    def __iter__(self):
        return self

    def __next__(self):
        self.x -= 1
        if self.x <= 0:
            raise StopIteration
        return '#' * self.x


import time

# главная программа с заголовком,
# позволяющим использовать этот файл как модуль:
if __name__ == '__main__':
    # создание итерируемого объекта
    main_iter = RangeIterableIterator(32)
    # проход по итерируемому объекту с помощью цикла
    for line in main_iter:
        # вывод текущего элемента (который возвращает итератор)
        print(line)
        time.sleep(0.25)
