import math
from math import pi
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.sin(x)


# Создаём экземпляр класса figure и добавляем к Figure область Axes
fig, ax = plt.subplots()
# Добавим заголовок графика
ax.set_title('')
# Название оси X:
ax.set_xlabel('x')
# Название оси Y:
ax.set_ylabel('y')
# Начало и конец изменения значения X, разбитое на 100 точек
x = np.linspace(0, 2*pi, 100) # X от -5 до 5
# Построение функции
y = np.sin(x)
# Вывод графика
ax.plot(x, y)

#построение прямой у = 0
x1 = np.linspace(0, 2*pi, 100)
y1 = 0*x
ax.plot(x1, y1, color=(0, 0, 0))


#принятие входных данных
number_of_points = int(input())
type_of_equipment = input()
#подсчет мелкости равномерного разбиения
delta_x = 2*pi/(number_of_points-1)

#декларация и инициализация списка точек разбиения
list_of_points = []
for i in range(number_of_points):
    list_of_points.append(0 + i*delta_x)

#декларация и инициализация списков точек трех оснащений
right_equipment = list_of_points[1:number_of_points]
central_equipment = []
left_equipment = list_of_points[0:number_of_points-1]
for i in range(number_of_points-1):
    central_equipment.append((list_of_points[i+1] + list_of_points[i])/2)

#подсчет интегральной суммы в зависимости от выбранного оснащения
integral_sum = 0
if type_of_equipment == "left":
    for point in left_equipment:
        integral_sum += f(point) * delta_x
    #построение изображения интегральной суммы
    for i in range(number_of_points-1):
        x2 = np.linspace(list_of_points[i], list_of_points[i + 1], 100)
        y2 = 0 * x + np.sin(list_of_points[i])
        ax.plot(x2, y2, color=(1, 0, 0))
elif type_of_equipment == "right":
    for point in right_equipment:
        integral_sum += f(point) * delta_x
    for i in range(number_of_points-1):
        x2 = np.linspace(list_of_points[i], list_of_points[i + 1], 100)
        y2 = 0 * x + np.sin(list_of_points[i+1])
        ax.plot(x2, y2, color=(1, 0, 0))
else:
    for point in central_equipment:
        integral_sum += f(point) * delta_x
    for i in range(number_of_points-1):
        x2 = np.linspace(list_of_points[i], list_of_points[i + 1], 100)
        y2 = 0 * x + np.sin(central_equipment[i])
        ax.plot(x2, y2, color=(1, 0, 0))
print(integral_sum)
plt.show()
