---
type: assignment
date: 2024-01-16T14:00:00-0600
title: C++ and Make
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: GitHub Classroom Not Open Yet!
due_event: 
    type: due
    date: 2024-01-19T14:00:00-0600
    description: C++ and Make Due
---
# Prime Number Calculation and Performance Analysis

Write a C++ program to calculate prime numbers within a given range. You will then analyze the performance of your solution by collecting and discussing data on execution time for varying problem sizes.

**Programming Notes:**

1. Your program must ask the user to input two integers: the start and end of a range within which you will find all prime numbers.

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

3. Your main function should time the execution of the prime calculation and print out the time taken along with the primes found.

4. Collect data on execution times for at least five different range sizes and document your findings.

5. A brief report discussing your findings on how the problem size affects execution time.

When your program is ready for grading, ***commit*** and ***push*** your local repository to the remote git classroom repository and follow the _**Assignment Submission Instructions**_. 
