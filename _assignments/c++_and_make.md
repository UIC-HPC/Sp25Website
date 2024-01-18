---
type: assignment
date: 2024-01-16T14:00:00-0600
title: C++ and Make
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/2TQINBWg
due_event: 
    type: due
    date: 2024-01-23T14:00:00-0600
    description: C++ and Make Due
---
# Prime Number Calculation and Performance Analysis (25 points)

Write a C++ program to calculate prime numbers within a given range. You will then analyze the performance of your solution by collecting and discussing data on execution time for varying problem sizes.

**Material Needed:**
- Chrono Library ([c++.com](https://cplusplus.com/reference/chrono/))

```c++
    #include <chrono>

    // some code ...

    // start timing
    auto start = std::chrono::high_resolution_clock::now();
    someFunction();
    // stop timing
    auto stop = std::chrono::high_resolution_clock::now();

    // calculate the duration
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

    // output the duration
    std::cout << "Time taken by function: " << duration.count() << " milliseconds" << std::endl;

    // some more code ...
``` 
- Makefile ([Makefile Tutorial](https://makefiletutorial.com))

**Programming Notes:**

1. Your program must ask the user to input two integers: the start and end of a range, within which you will find all prime numbers (prime.cc).

2. Implement a function that determines whether a number is prime.

Pseudocode for calculation of a prime number:

```mathematica
Function isPrime(number):
    If number ≤ 1 Then
        Return False
    End If

    For i = 2 To √number (inclusive) Do
        If number mod i = 0 Then
            Return False
        End If
    End For

    Return True
End Function
```

3. Time the execution of the prime calculation in your main function and print out the time taken along with the number of primes found.

4. Create and add a **Makefile** to your repository to build **prime.cc** into an executable **prime** when `make` is executed.

5. Collect data on execution times for at least five different range sizes and document your findings; this will just be a text file (**timings.dat**).

6. Write a few sentences discussing your findings on how the problem size affects execution time (**report.txt**).

7. Make sure you have committed all the material to your repository.

When your program is ready for grading, ***commit*** and ***push*** your local repository to the remote git classroom repository and follow the _**Assignment Submission Instructions**_. 
