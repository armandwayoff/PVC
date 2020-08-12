import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from random import *
from math import *


def dist(v1, v2):
    return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)


def total_distance(lst):
    d = 0
    for j in range(len(lst) - 1):
        d += dist(lst[j], lst[j + 1])
    return d


def simulated_annealing(population,
                        initial_temperature,
                        alpha,
                        number_of_markov_chains,
                        length_of_markov_chains,
                        loop=True):

    def reverse_sublist(lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        return lst

    temperature = initial_temperature
    path = population.copy()
    if loop:
        path.append(population[0])
    record_distance = total_distance(path)
    for _ in range(number_of_markov_chains):
        temperature *= alpha
        for _ in range(length_of_markov_chains):
            selected_vertices = sample(range(1, len(population) + 1), 2)
            test = path.copy()
            test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
            test_distance = total_distance(test)
            if test_distance < record_distance:
                record_distance = test_distance
                path = test
            else:
                r = uniform(0, 1)
                if r < exp((record_distance - test_distance) / temperature):
                    record_distance = test_distance
    return path


X = [9.241551413031429, 9.324698805233636, 5.337992887487738, 3.5520407631408766, 2.5404657866784595, 4.137710240752574, 5.871889683941168, 1.0359652434546118, 7.8590662064219945, 0.8484660402216182, 6.951713588655457, 4.6132175153299855, 6.514271713989955, 9.433726199234652, 9.767235369004066, 2.89301856476355, 6.075225701917822, 8.261050667724275, 5.289217908860222, 5.83848787452336, 2.6728269920718537, 3.1685193295147474, 4.36253972879605, 7.763716614566438, 2.0150862611668163, 7.338402670936452, 6.655672181093001, 5.619441380136991, 0.8098332834371558, 8.528115946732635, 4.265270193088329, 7.645235678728559, 3.48037581805455, 1.943543719248072, 2.575690468272561, 1.1017060217252006, 2.519598292916929, 1.4943195508600549, 5.838088122135304, 5.349262556326266, 6.937970161957995, 1.0663632022665448, 4.4062184603821395, 7.571558218058742, 5.909000370804276, 2.4678702534232775, 4.215391285350623, 9.10770161190713, 7.385580102836199, 0.042742320977706694]
Y = [1.8174983702998215, 5.395829754918528, 0.5220656289380043, 5.668768081252331, 8.928423990204061, 1.2160174229207676, 1.5209803780839237, 6.589522336062478, 0.2751492483398976, 0.6276979441280606, 0.05617588266150664, 3.11950767145197, 5.762447513609352, 1.8049522913930338, 4.195661120852199, 0.44523464711135885, 7.127157569962704, 2.2051239405016543, 9.387320274489756, 1.4792539317732234, 0.7558187297666541, 0.8262147840816281, 7.302488147218922, 7.704279443064611, 3.3692774814049518, 5.683606275061448, 2.3995645622184982, 8.958473072977597, 3.9737873849533747, 3.3301043742759306, 9.309150356952317, 7.178616602832003, 3.0462246476847756, 8.189228533030658, 1.3797715300132185, 1.239805745095961, 0.15810405367055913, 8.173202028814114, 6.158369411680095, 4.77017360990767, 1.5234277393017015, 6.926856375268122, 1.7235090203721781, 6.561183500994372, 8.178651519438628, 7.944194910993174, 6.8391143268398125, 2.606638338386573, 9.735256121316278, 5.878941009285993]

NUMBER_VERTICES = 50
vertices = []

for i in range(NUMBER_VERTICES):
    new_vertex = Vertex(X[i], Y[i])
    vertices.append(new_vertex)

a = []
for i in range(5):
    path = simulated_annealing(vertices, 100, .99, 10 ** 3, 500)
    plt.figure(i)
    print(total_distance(path))
    for i in range(len(path) - 1):
        plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
    for vertex in vertices:
        plt.plot(vertex.x, vertex.y, 'bo')

plt.show()
