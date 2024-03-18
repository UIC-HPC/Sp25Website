---
type: assignment
date: 2024-04-04T14:00:00-0500
title: A09 - MPI Data Distribution and Collective Operations
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
#classroom: ../../static_files/not-yet.html
due_event: 
    type: due
    date: 2024-04-09T14:00:00-0500
    description: MPI Data Distribution and Collective Operations Due
---
<!-- This is a sample assignment. (25 points)-->

# MPI Data Distribution and Collective Operations Assignment

## Objective
Learn to utilize MPI's collective communication capabilities and understand data distribution among multiple processes. Implement a program that evenly distributes an array of integers across all MPI processes. Each process calculates the sum of its assigned integers, and a collective operation is used to compute the total sum across all processes. The root process will then print the total sum.

## Starter Code
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

## Instructions

1. Ensure you have a C++ compiler and the MPI library installed on your system.
2. Modify `datadistribution.cc` to distribute the array of integers and perform the sum across all processes.
3. Create a Makefile to compile program.
4. Create a `datadistribution.pbs` PBS script for running your program.
5. Submit your job using the `qsub` command if on ACER Extreme.
6. Reflect on what you have learned about parallel computing and MPI after completing the assignment.
7. Follow the semester-long guidelines for committing your changes, pushing to your repository, and issuing a pull request.

## Expected Learning Outcome

Students will gain a deeper understanding of MPI's collective operations and data distribution methods. This includes hands-on experience with distributing data across multiple processes, performing local computations, and using collective operations to aggregate results. Students will also learn to debug and optimize parallel programs for efficient data processing and communication.
