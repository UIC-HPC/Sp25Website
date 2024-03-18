---
type: assignment
date: 2024-04-11T14:00:00-0500
title: A10 - Hybrid Parallel Programming with MPI and OpenMP
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
#classroom: ../../static_files/not-yet.html
due_event: 
    type: due
    date: 2024-04-16T14:00:00-0500
    description: Hybrid Parallel Programming with MPI and OpenMP Due
---
<!-- This is a sample assignment. (25 points)-->
# Hybrid Parallel Programming with MPI and OpenMP Assignment

## Objective
Familiarize yourself with hybrid parallel programming by leveraging MPI for inter-process communication and OpenMP for intra-process threading. Implement a program to calculate the numerical integration of a function using the trapezoidal rule, distributing the computation among MPI processes and further parallelizing it within each process using OpenMP threads.

## Starter Code
Below is the starter code for your assignment. Your task is to complete the missing parts of the code to achieve the objective.

```c++
#include <iostream>
#include <mpi.h>
#include <omp.h>

// Function to integrate
double f(double x) {
    return x * x; // Example: integrate x^2
}

// TODO: Use OpenMP to parallelize this function
// Trapezoidal rule for a segment
double trapezoidalRule(double (*func)(double), double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (func(a) + func(b));

    for (int i = 1; i < n; ++i) {
        sum += func(a + i * h);
    }
    return sum * h;
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    
    int worldSize;
    MPI_Comm_size(MPI_COMM_WORLD, &worldSize);

    int worldRank;
    MPI_Comm_rank(MPI_COMM_WORLD, &worldRank);

    // Define the domain of integration [a, b] and number of trapezoids
    double a = 0.0, b = 1.0;
    int n = 1000; // Total number of trapezoids

    // Calculate the range for this process
    double localA = a + (b - a) / worldSize * worldRank;
    double localB = local_a + (b - a) / worldSize;
    int localN = n / worldSize;

    // Calculate local integral
    double localIntegral = trapezoidalRule(f, localA, localB, localN);

    // TODO: Use MPI to gather and sum the local integrals into a global integral
    
    // Print the result from the root process
    if (worldRank == 0) {
        // TODO: Print the final integral value
    }

    MPI_Finalize();
}
```

## Instructions

1. Ensure your system is equipped with a C++ compiler and OpenMP support, along with an MPI library.
2. Expand the provided `hybridintegration.cc` to partition the domain among MPI processes and parallelize the computation using OpenMP.
3. Create a Makefile to compile program.
4. Create a `hybridintegration.pbs` PBS script for running your program.
5. Submit your job using the `qsub` command if on ACER Extreme.
6. Reflect on your learning experience regarding hybrid parallel computing with MPI and OpenMP after completing the task.
7. Adhere to the semester-long guidelines for code submission including commit, push, and pull request processes.

## Expected Learning Outcome

Students will gain hands-on experience with hybrid parallel programming, understanding how to effectively combine MPI and OpenMP for high-performance computing tasks. This includes practical skills in distributing computations across processes with MPI and exploiting multi-threading within processes using OpenMP, leading to an appreciation of multi-level parallelism in modern computing architectures.
