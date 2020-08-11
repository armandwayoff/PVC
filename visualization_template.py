import matplotlib.pyplot as plt
from random import *


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


NUMBER_VERTICES = 20
vertices = []

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(uniform(0, 10), uniform(0, 10))
    vertices.append(new_vertex)

path = 

for i in range(len(path) - 1):
    plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
for vertex in vertices:
    plt.plot(vertex.x, vertex.y, 'bo')

plt.show()
