from random import randint, sample
from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx
import time


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


# cluster's functions


def create_clusters(reference_elements, elements_to_organise):
    global target_index
    new_node_color = []
    new_clusters = [[] for _ in range(NUMBER_CLUSTERS)]  # initialisation of the clusters list
    for k in range(len(elements_to_organise)):
        record = dist(0, 0, WIDTH, HEIGHT)
        for j in range(len(reference_elements)):
            d = dist(elements_to_organise[k].x, elements_to_organise[k].y,
                     reference_elements[j].x, reference_elements[j].y)
            if d < record:
                record = d
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


# graph's functions


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(vertices[lst[j]].x, vertices[lst[j]].y, vertices[lst[j + 1]].x, vertices[lst[j + 1]].y)
    return d


def reverse_sublist(lst, start, end):
    lst[start:end + 1] = lst[start:end + 1][::-1]
    return lst


NUMBER_VERTICES = 30
NUMBER_CLUSTERS = 8  # up to 8
NUMBER_ITERATIONS = 10 ** 4
WIDTH = HEIGHT = 100  # dimension of the canvas
VERTEX_SIZE = 150
COLORS = ['orange', 'red', 'purple', 'green', 'black', 'grey', 'pink', 'cyan']

vertices = []
G = nx.Graph()

print("* 2-opt & K-means *")
print("Number of vertices :", NUMBER_VERTICES,
      "| Number of clusters :", NUMBER_CLUSTERS,
      "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")

start_time = time.time()
# creation of the vertices
for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(randint(1, WIDTH), randint(1, HEIGHT))
    vertices.append(new_vertex)
    G.add_node(i, pos=(new_vertex.x, new_vertex.y))
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
print("Clusters : ✓")
print("--- %s seconds ---" % (time.time() - start_time))
# --------------------------------------------------------------

# graphs
# --------------------------------------------------------------
for cluster in clusters:
    if len(cluster) > 2:
        path = [vertices.index(vertex) for vertex in cluster]  # initial path
        path.append(path[0])  # creation of the loop
        record_distance = dist(0, 0, WIDTH, HEIGHT) * NUMBER_VERTICES
        for i in range(NUMBER_ITERATIONS):
            selected_vertices = sample(range(1, len(path) - 1), 2)
            test = path.copy()
            test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
            test_distance = total_distance(test)
            if test_distance < record_distance:
                record_distance = test_distance
                path = test
        for i in range(len(cluster)):
            G.add_edge(path[i], path[i + 1])
    if len(cluster) == 2:
        G.add_edge(vertices.index(cluster[0]), vertices.index(cluster[1]))

print("Graphs : ✓")
print("--- %s seconds ---" % (time.time() - start_time))
# --------------------------------------------------------------

plt.figure(str(NUMBER_CLUSTERS) + "-means | Iteration " + str(iteration))
nx.draw(G, pos, node_size=VERTEX_SIZE, node_color=node_color, with_labels=True)
plt.show()
