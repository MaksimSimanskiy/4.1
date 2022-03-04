#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое число, целая часть числа; поле second — положительное целое число,
дробная часть числа. Реализовать метод multiply() — умножение на произвольное целое
число типа int. Метод должен правильно работать при любых допустимых значениях first и
second.
"""

class Rational:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if (self.first <= 0) or (self.second <= 0):
            raise ValueError()

    def read(self):
        self.first = int(input("Введите целую часть числа "))
        self.second = int(input("Введите дробную часть числа "))

    def display(self):
        print(f"Число с плавающей точкой {self.first}.{self.second}")

    def multiply(self, other):
        length = len(str(self.second))
        fractal = self.second / (10 ** length)
        fln = float((self.first + fractal) * other)
        print("Результат умножения - ", fln)


def make_rational(first, second):
    num = Rational(first, second)
    if (first <= 0) or (second <= 0):
        raise ValueError()
    else:
        return num.display()


if __name__ == '__main__':
    newTask = Rational(12, 55)
    newTask.display()
    newTask.multiply(5)
    make_rational(45, 34)
