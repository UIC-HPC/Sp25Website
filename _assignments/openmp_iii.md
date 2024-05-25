---
type: assignment
date: 2024-02-22T14:00:00-0600
title: A07 - Strong and Weak Scaling with OpenMP
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/lu7rpHfk
due_event: 
    type: due
    date: 2024-02-29T23:59:00-0600
    description: Strong and Weak Scaling with OpenMP
---
# Strong and Weak Scaling with Numerical Integration using OpenMP

## Objective
Understand and demonstrate the concepts of strong and weak scaling in parallel computing by performing numerical integration of a function using the trapezoidal rule.

## Starter Code
Below is the starter code for your assignment. Your task is to complete the missing part of the code.

```c++
#include <omp.h>
#include <iostream>
#include <cmath>

double f(double x) {
    return std::sin(x); // Example function to integrate
}

double trapezoidal_rule(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (f(a) + f(b));

    // TODO: Use OpenMP to parallelize this loop with proper scheduling
    for (int i = 1; i < n; ++i) {
        sum += f(a + i * h);
    }

    return h * sum;
}

int main() {
    double a = 0;       // Lower bound of integration
    double b = M_PI;    // Upper bound of integration
    int n = 1e6;        // Number of trapezoids

    double integral = trapezoidal_rule(a, b, n);
    std::cout << "Integral: " << integral << std::endl;

    return 0;
}
```

## Instructions

1. **Parallelize the Calculation:** Enhance the provided code using OpenMP to parallelize the trapezoidal rule calculation. Focus on choosing an effective scheduling strategy for balanced load distribution.
2. **Strong Scaling Analysis:** Demonstrate strong scaling by keeping the total problem size constant while varying the number of threads. Record and analyze the performance impact.
3. **Weak Scaling Analysis:** Show weak scaling by increasing the problem size in proportion to the number of threads. This analysis should demonstrate how the system's efficiency varies with increasing workload and parallelism.
4. **Data Collection:** Compile the program using `g++ -fopenmp openmp02.cc -o openmp02` or create a Makefile. Execute your program with different thread counts and problem sizes, recording execution times for analysis. (**_openmp02_**)
5. **Plotting Results:** Plot the execution times against the number of threads for both strong and weak scaling analyses. Use graphing software or scripting tools like Python with Matplotlib to create your plots. This will visually demonstrate the scaling behavior and efficiency of your parallel implementation. (**_openmp02-strong.png_** and **_openmp02-weak.png_** or combined graph **_openmp02-scaling.png_**)

## Expected Learning Outcomes

- It is essential to have a comprehensive understanding of the concepts of strong and weak scaling within the context of parallel computing.
- Practical experience optimizing parallel code to enhance performance is crucial for practical parallel computing.
- Developing the ability to analyze and interpret the impact of different scaling strategies on parallel execution efficiency is valuable for identifying optimal parallelization approaches.
- Proficiency in visualizing performance data through plotting is essential for effectively communicating the results of parallel execution and scaling analysis.
