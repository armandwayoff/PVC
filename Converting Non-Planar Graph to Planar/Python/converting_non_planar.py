from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intersection(p1, p2, q1, q2):
    det = (p2.x - p1.x) * (q2.y - q1.y) - (q2.x - q1.x) * (p2.y - p1.y)
    if det == 0:
        return False
    else:
        lamb = ((q2.y - q1.y) * (q2.x - p1.x) + (q1.x - q2.x) * (q2.y - p1.y)) / det
        gamma = ((p1.y - p2.y) * (q2.x - p1.x) + (p2.x - p1.x) * (q2.y - p1.y)) / det
        return (0 < lamb < 1) and (0 < gamma < 1)


def calc():
    number_intersections = 0
    for i in range(len(vertices) - 2):
        for j in range(i + 2, len(vertices) - 1):
            if i != j and (i + 1) != j:
                inter = intersection(vertices[i], vertices[i + 1], vertices[j], vertices[j + 1])
                if inter:
                    vertices[i + 1], vertices[j] = vertices[j], vertices[i + 1]
                    path[i + 1], path[j] = path[j], path[i + 1]
                    number_intersections += 1
    if number_intersections != 0:
        return True
    else:
        return False
    

number_vertices = 5
width = height = 10  # dimension of the canvas

vertices = []
path = []

print("Vertices coordinates :")
for i in range(number_vertices):
    vertices.append(Vertex(randint(0, width), randint(0, height)))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")
    path.append(i)  # the vertices are initially linked in their order of generation

while calc():
    calc()

print("Path :", path)
print("Adjacency matrix :")
adjacency_matrix = [[0 for col in range(number_vertices)] for row in range(number_vertices)]
for i in range(number_vertices - 1):
    adjacency_matrix[path[i]][path[i + 1]] = 1
    adjacency_matrix[path[i + 1]][path[i]] = 1
for row in adjacency_matrix:
    print(*row)
    
