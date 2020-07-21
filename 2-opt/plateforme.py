import matplotlib.pyplot as plt
import networkx as nx
from random import randint, sample
from math import sqrt


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def create_clusters(reference_elements, elements_to_organise):
    global target_index
    new_node_color = []
    new_clusters = [[] for _ in range(NUMBER_CLUSTERS)]  # initialisation of the clusters list
    for k in range(len(elements_to_organise)):
        record_distance = dist(0, 0, WIDTH, HEIGHT)
        for j in range(len(reference_elements)):
            d = dist(elements_to_organise[k].x, elements_to_organise[k].y,
                     reference_elements[j].x, reference_elements[j].y)
            if d < record_distance:
                record_distance = d
                target_index = j
        new_clusters[target_index].append(elements_to_organise[k])
        new_node_color.append(COLORS[target_index])
    return new_clusters, new_node_color


def centroid_of(lst):
    xG = yG = 0
    for a in range(len(lst)):
        xG += lst[a].x / len(lst)
        yG += lst[a].y / len(lst)
    return Centroid(xG, yG)


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(vertices[lst[j]].x, vertices[lst[j]].y, vertices[lst[j + 1]].x, vertices[lst[j + 1]].y)
    return d


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


NUMBER_VERTICES = 50
NUMBER_CLUSTERS = 4
NUMBER_ITERATIONS = 10 ** 5
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150
COLORS = ['orange', 'red', 'purple', 'green', 'black', 'grey', 'pink', 'cyan']

vertices = []
G = nx.Graph()

print("* K-means *")
print("Number of vertices :", NUMBER_VERTICES,
      "| Number of clusters :", NUMBER_CLUSTERS,
      "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")

# creation of the vertices
# print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(1, WIDTH), randint(1, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
    # print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")
procurement_platform = Vertex(WIDTH / 2, HEIGHT / 2)
G.add_node("platform", pos=(procurement_platform.x, procurement_platform.y))
pos = nx.get_node_attributes(G, 'pos')

# initialisation
initial_vertices = sample(vertices, NUMBER_CLUSTERS)

clusters, node_color = create_clusters(initial_vertices, vertices)

# clusters
# --------------------------------------------------------------
previous_state = clusters
current_state = []
iteration = 0
while previous_state != current_state:
    previous_state = clusters
    current_state = []
    centroids = []
    for cluster in clusters:
        centroids.append(centroid_of(cluster))
    clusters, node_color = create_clusters(centroids, vertices)
    current_state = clusters
    iteration += 1
print("Clusters : done")
# --------------------------------------------------------------

# graphs
# --------------------------------------------------------------
for cluster in clusters:
    path = []
    for vertex in cluster:
        path.append(vertices.index(vertex))
    record_distance = dist(0, 0, WIDTH, HEIGHT) * NUMBER_VERTICES
    for i in range(NUMBER_ITERATIONS):
        selected_vertices = sample(range(NUMBER_VERTICES), 2)
        test = path.copy()
        test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
        test_distance = total_distance(test)
        if test_distance < record_distance:
            record_distance = test_distance
            path = test
    for i in range(len(cluster) - 1):
        G.add_edge(path[i], path[i + 1])
print("Tours : done")
# --------------------------------------------------------------

node_color.append('black')
plt.figure(str(NUMBER_CLUSTERS) + "-means | Iteration " + str(iteration))
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color=node_color)
plt.show()
