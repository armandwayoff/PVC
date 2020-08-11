from math import *


def nearest_neighbour(population, starting_vertex):  
    def dist(v1, v2):
        return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    visited_vertices = [population[starting_vertex]]
    path = [population[starting_vertex]]
    current_vertex = population[starting_vertex]
    nearest_vertex = current_vertex

    while len(visited_vertices) < len(population):
        record_distance = float('inf')
        for vertex in population:
            if vertex not in visited_vertices:
                d = dist(vertex, current_vertex)
                if d < record_distance:
                    nearest_vertex = vertex
                    record_distance = d
        visited_vertices.append(nearest_vertex)
        path.append(nearest_vertex)
        current_vertex = nearest_vertex
    return path
