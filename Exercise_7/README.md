# Research Algorithms - Exercise 7

This folder contains the implementation for Exercise 7 of the Research Algorithms course.

## Contents

- `Ex7.py`: Main implementation file for the exercise questions
- `Q3 solution.png`: Solution image for Question 3

## Topics Covered

### Question 1: Linear System Solvers Performance Comparison

Comparison of the performance of NumPy and CVXPY for solving linear equation systems of various sizes.

### Question 2: Approximation Algorithm Analysis

Analysis of the approximation ratio of the maximum clique approximation algorithm in NetworkX.

### Question 3: Coding Game Challenge

Solution to the "The Lucky Number" challenge on CodinGame.

## Implementation Details

### Linear System Solvers Performance Comparison

This implementation compares the performance of two different approaches to solving linear equation systems:

- NumPy's built-in `linalg.solve` function
- CVXPY's constraint-based convex optimization approach

The program creates random linear equation systems of different sizes, solves them using both methods, and plots the runtime versus system dimension.

### Approximation Algorithm Analysis

This implementation analyzes the approximation ratio of NetworkX's maximum clique approximation algorithm compared to the exact solution. For random graphs of various sizes, it:

1. Generates a random graph with random edge probability
2. Finds the exact maximum clique size using a brute force algorithm
3. Finds an approximate maximum clique using NetworkX's approximation algorithm
4. Calculates and plots the ratio of the approximate solution size to the exact solution size

## Running the Code

```bash
# To run the experiments and generate plots
python Ex7.py
```

## Dependencies

- NumPy: For numerical operations and linear algebra
- CVXPY: For convex optimization
- Matplotlib: For plotting results
- NetworkX: For graph operations and clique algorithms
- random: For generating random systems
- timeit: For performance measurement