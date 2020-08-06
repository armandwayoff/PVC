import matplotlib.pyplot as plt
from random import *
from math import *


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(lst[j].x, lst[j].y, lst[j + 1].x, lst[j + 1].y)
    return d


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


NUMBER_VERTICES = 40
NUMBER_ITERATIONS = 10 ** 5

vertices = []
path = []

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(uniform(0, 10), uniform(0, 10))
    vertices.append(new_vertex)
    path.append(new_vertex)
path.append(vertices[0])

record_distance = total_distance(path)
for i in range(NUMBER_ITERATIONS):
    selected_vertices = sample(range(1, NUMBER_VERTICES + 1), 2)
    test = path.copy()
    test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
    test_distance = total_distance(test)
    if test_distance < record_distance:
        record_distance = test_distance
        path = test

for i in range(len(path) - 1):
    plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
for vertex in vertices:
    plt.plot(vertex.x, vertex.y, 'bo')

plt.show()
