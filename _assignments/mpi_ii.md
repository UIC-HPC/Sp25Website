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
# MPI Data Distribution and Collective Operations Assignment

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

## Instructions
1. Ensure you have a C++ compiler and the MPI library by loading the appropriate modules.
2. Modify the starter code to distribute the array of integers and perform the sum across all processes.
3. Create a Makefile to compile the program `datadistribution`, ensuring you have a `make all` and `make clean`.
4. Develop a `datadistribution.pbs` PBS script for running your program.
5. Submit your job using the `qsub` command on ACER Extreme resource.
6. Modify your program to measure the execution time of the parallel section, including the distribution of the array, local sum computation, and the collective operation to compute the total sum.
7. Execute your program on 1, 2, 4, and 8 nodes. Ensure consistency in the execution environment for comparability of results.
8. Analyze execution time data and create a graph plotting total execution time against the number of nodes. Include this graph in your submission.
9. Add the performance graph and your modified source code, Makefile, and PBS scripts to your repository.
10. Reflect on what you have learned about parallel computing and MPI after completing the assignment.
11. Follow the semester-long guidelines for committing changes, pushing to your repository, and issuing a pull request.

## Submission Guidelines
1. Ensure your code is properly documented and follows best practices.
2. Include all necessary files, including the modified source code, Makefile, PBS scripts, and the performance graph.
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
