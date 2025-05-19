# Research Algorithms - Exercise 5

This folder contains the implementation for Exercise 5 of the Research Algorithms course.

## Contents

- `Ex5.py`: Main implementation file for the exercise questions
- `Q3 Solution.jpeg`: Solution image for Question 3

## Topics Covered

### Question 1: Bounded Subsets Iterator

Implementation of a custom iterator class that efficiently generates all bounded subsets of a given list, where the sum of elements in each subset does not exceed a given bound.

### Question 2: Strategy Pattern for Graph Search

Implementation of a strategy pattern for graph search algorithms, allowing the use of either BFS or DFS to find paths and calculate distances in a graph.

### Question 3: Coding Game Challenge

Solution to the "Super Computer" challenge on CodinGame.

## Implementation Details

### Bounded Subsets Iterator

The bounded_subsets class provides an efficient iterator that generates all subsets of a list where the sum of elements doesn't exceed a specified bound. It maintains the following properties:

- Efficient generation without recursion or double-loops
- Sorted output for consistent iteration order
- Complete enumeration of all valid subsets

### Strategy Pattern for Graph Search

The shortest_path function implements the strategy pattern to use either BFS or DFS algorithms for finding paths in a graph. It features:

- Ability to choose between BFS and DFS algorithms at runtime
- Support for different input formats (tuples or lists)
- Different output formats (path or path length)

## Running the Code

```bash
# To run the doctests
python Ex5.py
```

## Dependencies

- networkx: For graph operations
- doctest: For inline testing