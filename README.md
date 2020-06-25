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
0 : ( 9 ; 4 )
1 : ( 36 ; 26 )
2 : ( 4 ; 23 )
3 : ( 45 ; 11 )
4 : ( 10 ; 13 )
5 : ( 15 ; 45 )
6 : ( 38 ; 44 )
7 : ( 9 ; 23 )
8 : ( 21 ; 12 )
9 : ( 0 ; 20 )
Path : [0, 4, 7, 2, 9, 8, 1, 3, 6, 5]
Adjacency matrix :
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
```
