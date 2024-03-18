---
type: assignment
date: 2024-03-28T14:00:00-0500
title: A08 - Hello World with MPI
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
#classroom: ../../static_files/not-yet.html
due_event: 
    type: due
    date: 2024-04-02T14:00:00-0500
    description: A08 - Hello World with MPI Due
---
# MPI Hello World in C++

## Objective
Learn the basics of parallel programming in C++ using the Message Passing Interface (MPI). Write a program that initializes the MPI environment and enables each process to print "Hello, World!" along with its rank in the `MPI_COMM_WORLD` communicator. This assignment must be conducted on **extreme.acer.uic.edu**. Remember, if you use the ACER resource, you must submit via a PBS script and avoid running directly on the login node.

## Expected Learning Outcomes
1. Understand fundamental concepts of parallel programming.
2. Gain proficiency in using MPI for process communication.
3. Learn how to initialize and finalize the MPI environment.
4. Develop the ability to write and execute simple parallel programs in a high-performance computing context.

## Starter Code (hellompi.cc)
Below is the starter code for your assignment. Your task is to complete the missing part of the code.

```c++
#include <mpi.h>
#include <iostream>

int main(int argc, char** argv) {
    // Initialize the MPI environment
    MPI_Init(&argc, &argv);

    // Get the number of processes
    int worldSize;
    MPI_Comm_size(MPI_COMM_WORLD, &worldSize);

    // Get the rank of the process
    int worldRank;
    MPI_Comm_rank(MPI_COMM_WORLD, &worldRank);

    // TODO: Modify this part to print "Hello World from rank X!",
    // where X is the rank of the process.
    std::cout << "Hello World" << std::endl;

    // Finalize the MPI environment.
    MPI_Finalize();
}
```

## Instructions

1. Ensure your environment is configured for MPI by loading the necessary modules, specifically OpenMPI using `module load OpenMPI`. You can verify the modules loaded with `module list`.
2. Complete the code to have each process print "Hello, World!" followed by its rank.
3. Create a `Makefile` for this program that builds the executable `hellompi`, as well as a `make all` and `make clean`. Make sure you add this file to your repository.
4. Compile the MPI program. 

### PBS Script (`hellompi.pbs`)

```bash
#!/bin/bash
#PBS -N hellompi              # Job name
#PBS -q edu_shared            # Queue name
#PBS -l nodes=4:ppn=1         # Request 4 nodes and 1 processor per node
#PBS -l walltime=00:01:00     # Maximum walltime for the job
#PBS -o hellompi.otxt         # Output file
#PBS -e hellompi.etxt         # Error file
#PBS -V                       # Export all environment variables to the job

cd $PBS_O_WORKDIR             # Navigate to the job submission directory

module load OpenMPI           # Load the OpenMPI module

mpirun -np 4 ./hellompi       # Execute the MPI program
```

4. If using the ACER resource, create a PBS script named `hellompi.pbs` for job submission. This script should manage module loading and program execution across 4 nodes.
5. Submit your job using the `qsub` command if on ACER Extreme.
6. Reflect on what you have learned about parallel computing and MPI after completing the assignment.
7. Follow the semester-long guidelines for committing your changes, pushing to your repository, and issuing a pull request.

## Submission Guidelines

1. Ensure your code is properly documented and follows best practices.
2. Include all necessary files, including the modified source code and the PBS script if applicable.
3. Follow the provided submission instructions for committing and pushing your changes.

## Evaluation Criteria

1. Correct implementation of MPI Hello World program.
2. Proper execution and output of the program.
3. Adherence to submission guidelines and coding standards.
4. Reflection on parallel computing and MPI.

## Reflection

Reflect on what you have learned about parallel computing and MPI after completing the assignment. Discuss any challenges faced and lessons learned during the process.

## Additional Resources

- [MPI Tutorial](https://mpitutorial.com/tutorials/)
- [Open MPI v4.1.6 Documentation](https://www.open-mpi.org/doc/current/)
- [Message Passing Interface (MPI)](https://computing.llnl.gov/tutorials/mpi/)
- [Man pages for MPI](https://www.mpich.org/static/docs/latest/)

