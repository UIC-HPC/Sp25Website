---
type: assignment
date: 2024-04-11T14:00:00-0500
title: A10 - Hybrid Parallel Programming with MPI and OpenMP
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/c5RzsZ-6
due_event: 
    type: due
    date: 2024-04-16T23:59:00-0500
    description: Hybrid Parallel Programming with MPI and OpenMP Due
---
# Hybrid Parallel Programming with MPI and OpenMP

## Objective
The objective of this assignment is to familiarize yourself with hybrid parallel programming by leveraging MPI for inter-process communication and OpenMP for intra-process threading. You will implement a program to calculate the numerical integration of a function using the trapezoidal rule, distributing the computation among MPI processes and further parallelizing it within each process using OpenMP threads.

## Expected Learning Outcomes
1. Gain hands-on experience with hybrid parallel programming.
2. Understand how to effectively combine MPI and OpenMP for high-performance computing tasks.
3. Acquire practical skills in distributing computations across processes with MPI.
4. Learn to exploit multi-threading within processes using OpenMP.
5. Develop an appreciation for multi-level parallelism in modern computing architectures.

## Starter Code (`hybridintegration.cc`)
Below is the starter code for your assignment. Your task is to complete the missing parts of the code to achieve the objective.

```c++
#include <iostream>
#include <mpi.h>
#include <omp.h>

// Functions to integrate
// Simple Polynomial
double f(double x) {
    return x * x;             // Integrate x^2
}

// Moderately Complex Function (Polynomial and Trigonometric)
double f1(double x) {
    return x * x * sin(x);    // Integrate x^2 * sin(x)
}

// Highly Complex Function (Exponential, Trigonometric, and Polynomial)
double f2(double x) {
    return exp(-x) * sin(x) * x * x; // Integrate e^(-x) * sin(x) * x^2
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

## Background
### The Trapezoidal Rule

The [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) is a numerical method for approximating the definite integral of a function over an interval <span style="display:inline-block;">$$[a, b]$$</span>. It works by dividing the interval into <span style="display:inline-block;">$$n$$</span> trapezoids, rather than rectangles, calculating the area of each trapezoid, and summing these areas to approximate the total integral. The formula is given by:

$$ Integral \approx \frac{h}{2} \left [ f(a) + 2 \sum_{k=1}^{n-1} f(a + kh) + f(b)  \right ] $$

where <span style="display:inline-block;">$$h = \frac{(b - a)}{n}$$</span> is the width of each trapezoid.

### Accuracy and the Role of <span style="display:inline-block;">$$n$$</span>
The accuracy of the trapezoidal rule is directly related to the number of trapezoids <span style="display:inline-block;">$$n$$</span> used. Increasing <span style="display:inline-block;">$$n$$</span> decreases the width <span style="display:inline-block;">$$h$$</span> of each trapezoid, leading to a more accurate approximation of the integral. However, this also increases the computational load. The challenge is to find a balance between accuracy and computational efficiency, especially in a parallel computing context.

## Instructions for Hybrid Parallel Programming Assignment
1. **Environment Preparation**: Load the necessary modules on the ACER Extreme system to ensure a C++ compiler with OpenMP support and an MPI library are available. Use the `module load` command to prepare your environment with the appropriate tools for compiling and running your parallel programming assignment.
2. **Expand the Starter Code**: Begin with the `hybridintegration.cc` file provided to you. Extend this code to distribute the computational workload across multiple MPI processes. Within each of these processes, further parallelize the computation by employing OpenMP. This method leverages the combined power of MPI and OpenMP for efficient parallel computation.
3. **Compile Using Makefile**: Construct a `Makefile` to facilitate the compilation of your project. Ensure it includes `make all` for compiling the `hybridintegration` program and `make clean` for removing compiled binaries and other build artifacts. This setup makes building and cleaning your project straightforward.
4. **Generate PBS Script**: Develop a Portable Batch System (PBS) script named `hybridintegration.pbs` for executing your program on ACER's HPC resources. This script must specify the necessary computing resources, such as the number of nodes and processors per node, which are essential for executing your program in an HPC environment.
5. **Job Submission**: Submit your program for execution on the ACER Extreme system using the `qsub` command, providing your `hybridintegration.pbs` script as the argument. This action will queue your program for execution on the cluster.
6. **Performance Exploration**: Investigate how the performance of your program is influenced by varying the number of OpenMP threads and MPI ranks. Utilize the HPC resources to test different configurations, documenting the performance outcomes. Focus on identifying which combinations of thread counts and ranks result in optimal performance. Analyze and create graphs of these performance metrics to understand the scalability and efficiency of your program.
7. **Insight Visualization**: Produce plots that compare the performance and accuracy of integrating different functions. These plots should demonstrate the effects of computational complexity on your hybrid MPI/OpenMP solution's performance.
8. **Reflective Learning**: After completing your experiments, reflect on your experiences with hybrid parallel computing. Discuss any challenges you faced, how you addressed them, and what strategies proved effective. This reflection will deepen your understanding of working with MPI and OpenMP.
9. **Adherence to Submission Guidelines**: Follow the code submission guidelines set for this semester. Commit your code to GitHub, push your changes to a remote repository, and open a pull request for review. 

## Submission Guidelines
1. Ensure your code is properly documented and follows best practices.
2. Include all necessary files, including the modified source code, Makefile, PBS scripts, and the performance graph(s).
3. Follow the provided submission instructions for committing and pushing your changes.

## Evaluation Criteria
Submissions will be assessed based on several critical aspects. First, we'll evaluate the correct implementation of hybrid parallel programming using MPI and OpenMP, focusing on effective data distribution and parallelization. Next, we will test the program's functionality to ensure it executes appropriately and delivers accurate results. We will also check adherence to the submission guidelines and coding standards, providing high-quality code. Additionally, the quality of visualizations, such as plots depicting performance outcomes from varying thread and rank combinations, will be examined for clarity and insightfulness. Finally, we look forward to reading your reflections on the learning journey with hybrid parallel computing, including challenges faced and overcome. This evaluation aims to comprehensively understand your programming skills and problem-solving approach.

## Reflection
After completing the assignment:
1. Reflect on what you have learned about parallel computing and MPI.
2. Discuss any challenges faced and lessons learned during the process, and reflect on the scalability of your program based on the performance data gathered.
3. Discuss patterns observed and any modifications or optimizations made to improve performance.

## Additional Resources
- [MPI Tutorial](https://mpitutorial.com/tutorials/)
- [Open MPI v4.1.6 Documentation](https://www.open-mpi.org/doc/current/)
- [OpenMP - API Specification for Parallel Programming](https://www.openmp.org/spec-html/5.1/openmp.html)
- [Man pages for MPI](https://www.mpich.org/static/docs/latest/)
- [OpenMP Documentation](https://www.openmp.org/resources/openmp-specifications/)
