[![made-with-p5js](https://img.shields.io/badge/Made_with-p5.js-ED1F5E.svg)](https://p5js.org)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/armandwayoff/Travelling-Salesman-Problem/blob/master/LICENSE)

# Travelling Salesman Problem

## Table of Contents

* [Converting Non-Planar Graph to Planar](#converting-non-planar-graph-to-planar)
* [Nearest Neighbour Algorithm](#nearest-neighbour-algorithm)

## Converting Non-Planar Graph to Planar

* What's a [planar graph](https://en.wikipedia.org/wiki/Planar_graph) ?

This algorithm is a sub-algorithm that can be implemented in a more general algorithm for solving the travelling salesman problem.

The "Converting Non-Planar Graph to Planar" folder contains two versions, one in Python and one in JavaScript. Both versions generate a certain numbers of random vertices and then determine the path.

The Python version prints the coordinates of all the vertices, the path and the adjacency matrix. You can find an example below.

### Output Example

```
* Converting Non-Planar Graph to Planar *
Number of vertices : 10 | Dimensions of the canvas : (100 ; 100)

Vertices coordinates :
0 : (75 ; 10)
1 : (60 ; 89)
2 : (6 ; 11)
3 : (51 ; 46)
4 : (94 ; 44)
5 : (39 ; 0)
6 : (97 ; 84)
7 : (68 ; 73)
8 : (34 ; 94)
9 : (1 ; 66)
Path : [0, 4, 5, 2, 7, 3, 6, 1, 8, 9]
Adjacency matrix :
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0 1 0
0 0 0 0 0 1 0 1 0 0
0 0 0 0 0 0 1 1 0 0
1 0 0 0 0 1 0 0 0 0
0 0 1 0 1 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 1 0
```
