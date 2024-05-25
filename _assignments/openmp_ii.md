---
type: assignment
date: 2024-02-15T14:00:00-0600
title: A06 - Parallel Reduction with Performance Analysis
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/SwVRsUJi
due_event: 
    type: due
    date: 2024-02-22T23:59:00-0600
    description: Parallel Reduction with Performance Analysis Due
---
# Advanced C++ OpenMP Assignment: Parallel Reduction with Performance Analysis

## Objective

This assignment aims to deepen your understanding of OpenMP's parallel loop constructs, the concept of reduction, and the impact of thread count on performance. You will implement a parallel version of array summation and analyze how execution time varies with different numbers of threads.

## Starter Code

Below is the starter code for your assignment. Your task is to complete the missing part of the code and extend it to measure performance.

```c++
#include <omp.h>
#include <iostream>
#include <vector>

int main() {
    const int SIZE = 1e6;
    std::vector<int> numbers(SIZE, 1); // Initialize all elements to 1
    int total_sum = 0;

    // Parallel region begins here
    #pragma omp parallel 
    {
        // TODO: Use 'omp for' and 'reduction' to calculate the sum of the array
    }
    
    std::cout << "Total sum is " << total_sum << std::endl;
    return 0;
}
```

## Instructions

1. **Complete the Parallel Region:** Use the omp for directive and reduction clause to calculate the sum in parallel.
2. **Performance Measurement:** Modify the program to measure and record the execution time for the parallel region with varying numbers of OpenMP threads (1, 2, 4, 8). Use omp_set_num_threads() to set the thread count and omp_get_wtime() to measure execution time.
3. **Compilation and Execution:** Compile the code using `g++ -fopenmp openmp01.cc -o openmp01` or create a Makefile. Run the compiled program multiple times, each with a different number of threads, and collect the execution time data. (**_openmp01_**)
4. **Graphical Analysis:** Plot the recorded execution times against the number of threads. This graph should help visualize the performance scalability with the increase in thread count. (**_openmp01.png_**)
5. **Discussion Questions:** Reflect on the observed performance changes with varying thread counts. Consider the impact of thread management overhead, the potential for diminishing returns, and the effect of hardware on performance scalability. (**_openmp01.txt_**)

## Expected Learning Outcomes

- An understanding of parallel loops, race conditions, and the application of the reduction clause in OpenMP is essential.
- The ability to measure and analyze the performance impact of altering the number of threads in a parallel program is crucial.
- Gaining insights into the scalability and efficiency of parallel computing with OpenMP is valuable for optimizing performance.

## Advanced Challenge (Optional)

Explore the impact of different scheduling strategies (static, dynamic) on performance. Modify the parallel loop to specify the scheduling strategy and compare the execution times with those obtained using the default setting. (**_openmp01a.txt_** and **_openmp01a.png_**)

