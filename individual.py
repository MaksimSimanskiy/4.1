#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое число, целая часть числа; поле second — положительное целое число,
дробная часть числа. Реализовать метод multiply() — умножение на произвольное целое
число типа int. Метод должен правильно работать при любых допустимых значениях first и
second.
"""

class Task:

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


    def make_multiply(self, other):
        fln = float(str(self.first) + "." + str(self.second))
        c = fln * other
        print("Результат умножения - ", c)


if __name__ == '__main__':
    newTask = Task(12, 5)
    newTask.read()
    newTask.display()
    newTask.multiply(5)
