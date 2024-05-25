---
type: assignment
date: 2024-04-04T14:00:00-0500
title: A09 - MPI Data Distribution and Collective Operations
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/DjZmQgZv
due_event: 
    type: due
    date: 2024-04-09T23:59:00-0500
    description: MPI Data Distribution and Collective Operations Due
---
# MPI Data Distribution and Collective Operations

## Objective
This assignment aims to learn to utilize MPI's collective communication capabilities and understand data distribution among multiple processes. Students will implement a program that evenly distributes an array of integers across all MPI processes. Each process calculates the sum of its assigned integers, and all processes collectively compute the total sum. The root process will then print the total sum.

## Expected Learning Outcomes
1. Gain a deeper understanding of MPI's collective operations and data distribution methods.
2. Acquire hands-on experience with distributing data across multiple processes.
3. Learn to perform local computations and use collective operations to aggregate results.
4. Develop skills in debugging and optimizing parallel programs for efficient data processing and communication.

## Starter Code (datadistribution.cc)
Below is the starter code for your assignment. Your task is to complete the missing parts of the code to achieve the objective.

```c++
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int worldSize;
    MPI_Comm_size(MPI_COMM_WORLD, &worldSize);

    int worldRank;
    MPI_Comm_rank(MPI_COMM_WORLD, &worldRank);

    // Define the array size and the array elements
    int arraySize = 100; // Example size
    std::vector<int> array;
    
    // TODO: Initialize the array with values if rank == 0
    // and then distribute it evenly across all processes
    
    // Each process will store its portion of the array in subArray
    std::vector<int> subArray;

    // TODO: Distribute the array to all processes and store the portion in subArray
    
    // TODO: Each process calculates the sum of its portion of the array
    
    // TODO: Use an MPI collective operation to calculate the total sum
    
    // TODO: Print the total sum from the root process
    
    MPI_Finalize();
}
```

## Instructions for Data Distribution and Summation Assignment

1. **Environment Preparation**: Load the necessary modules on the ACER Extreme system to access a C++ compiler and an MPI library. Utilize the `module load` command to equip your environment with the tools required for compiling and running your assignment on parallel programming.
2. **Modify the Starter Code**: Start with the provided starter file. Your task is to alter this code to distribute an array of integers across multiple MPI processes and perform the summation across all these processes efficiently.
3. **Compile Using Makefile**: Create a `Makefile` that eases the compilation process of your project. Ensure it includes `make all` for compiling the `datadistribution` program and `make clean` to remove any compiled binaries and build artifacts. This facilitates an organized and efficient build process.
4. **Generate PBS Script**: Craft a Portable Batch System (PBS) script named `datadistribution.pbs` to run your program using ACER's High-Performance Computing (HPC) resources. This script should outline the required computing resources, like the number of nodes and processors per node, critical for your program's execution on an HPC system.
5. **Job Submission**: Employ the `qsub` command to submit your program for execution on the ACER Extreme system, with your `datadistribution.pbs` script as the parameter. This will place your program in the queue for execution on the cluster.
6. **Performance Exploration**: Adjust your program to record the execution time of the parallel section, which includes the array distribution, local sum calculation, and the collective operation for the total sum computation. This step is crucial for performance analysis. Run your program on different node configurations: 1, 2, 4, and 8 nodes. Ensure that the execution environment remains consistent across these runs to maintain result comparability.
7. **Data Analysis and Visualization**: Analyze the collected execution time data and plot a graph showing the total execution time against the number of nodes used. This graph is an essential part of your submission, as it provides visual insight into the scalability of your solution.
8. **Reflective Learning**: Upon completing your experiments, reflect on your journey with parallel computing and MPI. Discuss the challenges encountered, solutions devised, and insights gained. This reflection fosters a deeper understanding of parallel computing concepts and MPI.
9. **Follow Submission Guidelines**: Adhere to the established guidelines for code submission throughout the semester. This includes committing your changes to GitHub, pushing them to a remote repository, and initiating a pull request for review.

## Submission Guidelines
1. Ensure your code is properly documented and follows best practices.
2. Include all necessary files, including the modified source code, Makefile, PBS scripts, and the performance graph(s).
3. Follow the provided submission instructions for committing and pushing your changes.

## Evaluation Criteria
Submissions will be evaluated based on a few important criteria. First, we'll examine how well the program uses MPI to distribute data and perform collective operations, ensuring it works as expected. Next, we'll check that the program runs correctly and produces the right results. Following this, we'll see if the submission follows the provided guidelines and standards for coding. We also want to read your thoughts on what you learned about parallel computing and MPI, especially any challenges you faced and overcame. Lastly, we'll look at how you gathered and analyzed performance data and how well you presented this information in a graph. This approach helps us see your programming skills and how you think about and solve problems.

## Reflection
After completing the assignment:
1. Reflect on what you have learned about parallel computing and MPI.
2. Discuss any challenges faced and lessons learned during the process, and reflect on the scalability of your program based on the performance data gathered.
3. Discuss patterns observed and any modifications or optimizations made to improve performance.

## Additional Resources
- [MPI Tutorial](https://mpitutorial.com/tutorials/)
- [Open MPI v4.1.6 Documentation](https://www.open-mpi.org/doc/current/)
- [Message Passing Interface (MPI)](https://computing.llnl.gov/tutorials/mpi/)
- [Man pages for MPI](https://www.mpich.org/static/docs/latest/)
