---
type: assignment
date: 2024-03-28T14:00:00-0500
title: A08 - Hello World with MPI
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/7TazeMsz
due_event: 
    type: due
    date: 2024-04-02T23:59:00-0500
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

## Instructions for MPI "Hello, World!" Assignment

1. **Environment Configuration**: Start by configuring your environment for MPI development. Load the necessary OpenMPI module with `module load OpenMPI`. Verify the loaded modules with `module list` to ensure everything is set up correctly.
2. **Code Completion**: Your task is to modify the provided starter code so that each process prints "Hello, World!" along with its MPI rank. This simple exercise will help you get acquainted with basic MPI commands and process management.
3. **Makefile Creation and Compile**: Develop a `Makefile` for your project to simplify the compilation process. This Makefile should facilitate building the executable named `hellompi` and include `make all` for compiling and `make clean` for removing compiled binaries and other artifacts. Ensure you commit this Makefile to your repository. Utilize the Makefile you created to compile the MPI program. This step transforms your source code into an executable, `hellompi`, ready for execution on the ACER Extreme HPC system.
4. **Job Submission**: With the `hellompi.pbs` script ready, submit your job to the ACER Extreme system using the `qsub` command. This action queues your program for execution according to the specifications in your PBS script. Prepare a PBS script named `hellompi.pbs` for job submission if you're using the ACER Extreme resource. This script is crucial for managing the job's execution environment, specifying the job's resource requirements, and ensuring the MPI program runs across multiple nodes.

    ```bash
    #!/bin/bash
    #PBS -N hellompi              # Job name
    #PBS -q edu_shared            # Queue name
    #PBS -l nodes=4:ppn=1         # Request 4 nodes and 1 processor per node
    #PBS -l walltime=00:01:00     # Maximum walltime for the job
    #PBS -o hellompi.otxt         # Output file name
    #PBS -e hellompi.etxt         # Error file name
    #PBS -V                       # Export all environment variables to the job

    cd $PBS_O_WORKDIR             # Change to the job submission directory
    module load OpenMPI           # Load the OpenMPI module
    mpirun -np 4 ./hellompi       # Execute the MPI program with 4 processes
    ```

5. **Reflective Learning**: After completing the assignment, take a moment to reflect on your learning experience with parallel computing and MPI. Consider the concepts you've grasped, the challenges you encountered, and how you addressed them. This reflection is an integral part of your learning process.
6. **Code Submission Guidelines**: Follow the established practices for code submission. Commit your changes, including the source code, Makefile, and PBS script, to your GitHub repository. Then, push these changes to a remote repository and create a pull request for review.

## Submission Guidelines

1. Ensure your code is properly documented and follows best practices.
2. Include all necessary files, including the modified source code and the PBS script if applicable.
3. Follow the provided submission instructions for committing and pushing your changes.

## Evaluation Criteria
Submissions will be assessed on key criteria. First, the correctness of the MPI Hello World program's implementation will be evaluated. Then, we'll check the program for proper execution and accurate output. Third, adherence to submission guidelines and coding standards will be reviewed. Lastly, your reflections on learning and challenges with parallel computing and MPI will be considered, providing insights into your problem-solving process.

## Reflection
After completing the assignment:
1. Reflect on what you have learned about parallel computing and MPI.
2. Discuss any challenges faced and lessons learned during the process.

## Additional Resources

- [MPI Tutorial](https://mpitutorial.com/tutorials/)
- [Open MPI v4.1.6 Documentation](https://www.open-mpi.org/doc/current/)
- [Message Passing Interface (MPI)](https://computing.llnl.gov/tutorials/mpi/)
- [Man pages for MPI](https://www.mpich.org/static/docs/latest/)
