# Travelling Salesman Problem

My Work on the Travelling Salesman Problem

## Table of Contents

* [Converting Non-Planar Graph to Planar](#converting-non-planar-graph-to-planar)
* [Nearest Neighbour Algorithm](#nearest-neighbour-algorithm)
  * [Output Example](#output-example)
  * [Visualisation of the Algorithm](#visualisation-of-the-algorithm)

## Converting Non-Planar Graph to Planar

* What's a [Planar graph](https://en.wikipedia.org/wiki/Planar_graph) ?

This algorithm is a sub-algorithm that can be implemented in a more general algorithm for solving the travelling salesman problem.

## Nearest Neighbour Algorithm

* What's the [Nearest neighbour algorithm](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm) ?

The nearest neighbor algorithm quickly yields a short tour, but usually not the optimal one. Therefor, it is not at all an optimal solution to the travelling salesman problem but can be used as an initialisation path.

The "Nearest Neighbor Algorithm" folder contains two versions, one in Python and one in JavaScript.
Both versions generate a certain numbers of random vertices and then determine the path. 

The Python version prints the coordinates of all the vertices, the path and the adjacency matrix. You can find an example [below](#output-example).

The purpose of the JavaScript version is to visualise the algorithm. The Javascript version is programmed with the [p5.js library](https://p5js.org/). This library is ideal because it has a full set of drawing functionality.

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

### Visualisation of the Algorithm

Example of implementation of the algorithm for ```15``` vertices generated randomly.

![NN1](illustration_images/NN1.png)
