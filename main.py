import math
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


def find_integral_rectangles_method(f, a, b, n):
    h = (b - a) / n
    quad = 0
    for i in range(1, n + 1):
        quad += f(a + i * h - h / 2)
    return quad * h


def find_integral_trapeze_method(f, a, b, n):
    h = (b - a) / n
    quad = 0
    for i in range(1, n):
        quad += f(a + i * h)
    quad += (f(a) + f(b)) / 2
    quad *= h
    return quad


def find_integral_parabola_method(f, a, b, n):
    h = (b - a) / n
    quad = 0
    for i in range(1, n, 2):
        quad += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        quad += 2 * f(a + i * h)
    quad += f(a) + f(b)
    quad *= h / 3
    return quad


def find_integral_gauss_method(f, a, b, n):
    f1 = f(((a + b) / 2) - ((b - a) / (2 * math.sqrt(3))))
    f2 = f(((a + b) / 2) + ((b - a) / (2 * math.sqrt(3))))
    quad = (b - a) / 2 * (f1 + f2)
    return quad


def func(x):
    # return pow(3, x) - 2 * x
    return (2 * (x * x) * math.sin(pow(x, 3) + 3 * x)) /  math.log(x + 1, math.e)


if __name__ == '__main__':
    left = 1
    right = 2
    v1 = integrate.quad(func, left, right)
    v2 = find_integral_rectangles_method(func, left, right, 10000)
    v3 = find_integral_trapeze_method(func, left, right, 10000)
    v4 = find_integral_parabola_method(func, left, right, 10000)
    v5 = find_integral_gauss_method(func, left, right, 10000)
    print('Точное значение       ', v1[0], '       разница с идеальным значением', abs(v1[0] - v1[0]))
    print('Метод Прямоугольников ', v2, '       разница с идеальным значением', abs(v2 - v1[0]))
    print('Метод Трапеций        ', v3, '       разница с идеальным значением', abs(v3 - v1[0]))
    print('Метод Парабол         ', v4, '       разница с идеальным значением', abs(v4 - v1[0]))
    print('Метод Гаусса          ', v5, '       разница с идеальным значением', abs(v5 - v1[0]))
