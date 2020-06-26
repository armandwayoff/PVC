# Travelling Salesman Problem

My Work on the Travelling Salesman Problem

## Table of Contents

* [Converting Non-Planar Graph to Planar](#converting-non-planar-graph-to-planar)
* [Nearest Neighbour Algorithm](#nearest-neighbour-algorithm)

## Converting Non-Planar Graph to Planar

* What's a [Planar graph](https://en.wikipedia.org/wiki/Planar_graph) ?

This algorithm is a sub-algorithm that can be implemented in a more general algorithm for solving the travelling salesman problem.

## Nearest Neighbour Algorithm

* What's the [Nearest neighbour algorithm](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm) ?

Example of implementation of the algorithm for 15 vertices generated randomly.

> By default, the algorithm starts with the first vertex.

![NN1](illustration_images/NN1.png)

### Output Example

Here is an output example with ```10``` vertices:

```
Vertices coordinates :
0 : (1 ; 48)
1 : (15 ; 33)
2 : (8 ; 3)
3 : (40 ; 26)
4 : (26 ; 35)
5 : (45 ; 1)
6 : (25 ; 8)
7 : (4 ; 24)
8 : (19 ; 35)
9 : (6 ; 31)
Path : [0, 9, 7, 1, 8, 4, 3, 6, 2, 5]
Adjacency matrix :
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
```
