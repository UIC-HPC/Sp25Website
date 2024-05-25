---
type: assignment
date: 2024-02-01T14:00:00-0600
title: A04 - Scalability of Threads in Quicksort
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/2cRS5gR4
due_event: 
    type: due
    date: 2024-02-08T23:59:00-0600
    description: Scalability of Threads in Quicksort
---

In this assignment, you will explore the scalability of multithreaded quicksort algorithms. Quicksort is a popular sorting algorithm, and we want to investigate how its performance scales with the number of threads. You will write C++ code to implement quicksort with multithreading, collect timing data, generate a graph using Python, and analyze the results.

## Learning Objectives

- Gain practical experience with multithreading in C++.
- Learn how to collect timing data for performance analysis.
- Understand the importance of multiple measurements for different thread counts.
- Visualize and interpret the scalability of multithreaded algorithms.

## Instructions

1. **Starter Code:** You will start with a provided C++ code template that implements quicksort with multithreading. The code template includes comments and directions for where you should add your timing and data collection code.

2. **Programming Tasks:** Follow the directions in the code to add timing code to measure the execution time of quicksort with varying numbers of threads. Collect timing data for different thread counts (e.g., 1, 2, 4, 8) and multiple experiments (at least 3 measurements for each thread count).

3. **Data Collection:** Store the timing data in a suitable data structure or output it to a file. Ensure that you collect enough data to analyze the scalability effectively.

4. **Python Graph:** Write a Python script to read the collected data and generate a graph (e.g., a line plot) to visualize the execution time versus the number of threads. Use a library like Matplotlib for graph generation.

5. **Analysis:** Write a paragraph or two to describe what you observe from the generated graph. Analyze how the execution time changes as the number of threads increases and discuss the concept of scalability. Explain any trends or anomalies in the data.

## Submission

Following the standard directions for class when using GitHubClassroom. Submit the following:

1. The completed C++ code with your timing and data collection additions.
2. The collected timing data (in a text file named `threads.dat`).
3. The Python script used to generate the graph (in a file named `threads.py`).
4. Graph produced by threads.py (in a file named `threads-graph.png`)
5. A paragraph or two of analysis explaining the results and scalability (in a text file named `threads.txt`).

## Evaluation Criteria

Your assignment will be evaluated based on the following criteria:

- Correct implementation of multithreaded quick sort.
- Proper timing and data collection code.
- Generation of a clear and accurate Python graph.
- Effective analysis of the scalability of multithreaded quick sort.
- Adherence to coding standards and proper documentation.

Have fun exploring the scalability of multithreaded algorithms!