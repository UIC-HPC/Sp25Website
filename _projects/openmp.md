---
type: project
date: 2024-02-07T23:59-0600
title: Parallel Painting
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
classroom: https://classroom.github.com/a/vYIIH5G_
due_event: 
    type: due
    date: 2024-03-08T23:59:00-0600
    description: Parallel Painting Project Due
---

<h2 style="text-align: center;">Weekly Speedup Challenge</h2>

<table style="width: 100%; border-collapse: collapse;">
    <tr>
        <th style="border: 1px solid black; padding: 8px; text-align: left;">Week</th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;" colspan="3">Results (speedup)</th>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;"><b>One</b> (02/19)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥇Seyfal Sultanov (34.0x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥈Kirk Tejas (6.0x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥉-</td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;"><b>Two</b> (02/26)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥇Seyfal Sultanov (53.2x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥈Kirk Tejas (6.0x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥉Soham Gumaste (3.7x)</td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;"><b>Three</b> (03/04)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥇Seyfal Sultanov (53.2x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥈Vishwa Sheth (43.9x)</td>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">🥉Soham Gumaste (23.0x)</td>
    </tr>
</table>
<br>

# Parallel Painting
#### A Mandelbrot Set Parallelization Project

## Overview
Implement a parallel version of the Mandelbrot set using OpenMP, explore the performance implications of different OpenMP features and settings, and conduct a scaling study to understand the performance benefits of parallel execution.

**Background:** The [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) is a fractal defined in the complex plane. For each point, $$c$$ in the complex plane, determine whether the iteratively defined sequence $$z_{n+1} = z_n^2 + c$$ remains bounded. The point $$c$$ is considered part of the Mandelbrot set if the sequence does not diverge to infinity typically checked within a fixed number of iterations.

## Objectives
- **Parallelize the Serial Code**: Implement a parallel version based on the provided Mandelbrot set serial code using OpenMP. Add appropriate code to the serial version to measure how long it takes to generate and write the Mandelbrot set to establish a baseline. Keep a version of your instrumented serial code. (**mandelbrot-serial.cc**)
- **Benchmark and Optimize**: Measure the performance of both serial and parallel versions to identify improvements. Aim to achieve the highest speedup relative to the serial execution for multiple iteration counts (500, 1000, 2000, 4000, 8000, 16000). All timings should be done with default values except the iteration count. (**mandelbrot.cc**)
- **Weekly Progress Submission**: Extra credit for submitting weekly progress to the project scoreboard. The top 3 students each week will receive extra credit. If you want to participate, create a branch of your code containing your latest results and submit the branch name and speedup using this [form](https://forms.office.com/r/rZBryMZQJX).
- **Final Submission Requirements**:
  - A **graph** demonstrating the speedup over base serial execution for multiple iteration counts (500 1000 2000 4000 8000 16000). (**mandelbrot.png**)
  - The **source code** of the final version, which must compile and run on `systems{1-4}.cs.uic.edu` resources. (**mandelbrot.cc** and **mandelbrot-serial.cc**)
  - **Summarize** your approach to parallelization with OpenMP and share what you learned throughout the project. (**mandelbrot.txt**)

## Project Requirements
- **Use of OpenMP**: Parallelization must be done exclusively with OpenMP.
- **Benchmarking**: Establish a baseline speed with the serial version and benchmark each improvement in the parallel version. Submit your best speedup overall - which is the average speedup across the six iteration counts (500, 1000, 2000, 4000, 8000, 16000); that means if you see a 2x performance increase on 500, 2.4x on 1000, and so on, such that you have a set of (2x, 2.4x, 3.0x, 3.1x, 2.9x, 2.7x) your average speedup is 2.7x. This is just for illustrative purposes. Base times for serial code that I will use to calculate speedup are as follows:
    - For 500 iterations: 11.18 seconds
    - For 1000 iterations: 19.51 seconds
    - For 2000 iterations: 34.63 seconds
    - For 4000 iterations: 64.91 seconds
    - For 8000 iterations: 128.11 seconds
    - For 16000 iterations: 253.70 seconds

You **may not change the size of the image** to get speedup; you may look at ways to improve I/O. You **must generate valid Mandelbrot set images**.

## Notes
The serial code and hence parallel code generate a `.pnm` image file; if you want to convert this file to `.png`, do so using `convert mandelbrot.pnm mandelbrot.png`. (Not currently installed on systems machines - I've asked to add it.)

## Grading
Grades will reflect the speed improvement of the parallelized code compared to the serial version. Higher speedups will lead to better grades.

## Ethics Statement
Collaboration is encouraged for learning and discussion, but direct code sharing is prohibited. Ensure your submissions are original and appropriately cite any external sources.

<h2 style="text-align: center;">Baseline Mandelbrot Performance Timings</h2>

<table style="width: 100%; border-collapse: collapse;">
    <tr>
        <th style="border: 1px solid black; padding: 8px; text-align: left;"><b>Iterations</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;"><b>Trial 1</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;"><b>Trial 2</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;"><b>Trial 3</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;"><b>Trial 4</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: center;"><b>Trial 5</b></th>
        <th style="border: 1px solid black; padding: 8px; text-align: right;"><b>Average</b></th>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">500</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">10.51s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">10.38s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">10.56s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">10.73s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">10.77s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>10.59s</b></td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">1000</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">19.80s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">18.97s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">17.80s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">18.19s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">19.17s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>18.79s</b></td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">2000</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">32.91s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">35.30s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">36.08s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">35.71s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">35.47s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>35.10s</b></td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">4000</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">65.39s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">65.86s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">66.94s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">68.73s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">67.69s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>66.92s</b></td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">8000</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">133.33s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">136.81s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">134.79s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">132.98s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">128.32s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>133.25s</b></td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 8px; text-align: left;">16000</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">263.33s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">258.65s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">260.77s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">254.36s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: center;">269.13s</td>
        <td style="border: 1px solid black; padding: 8px; text-align: right;"><b>261.25s</b></td>
    </tr>
</table>
<br>
*Measurements made on 02/21/2024 using systems2.cs.uic.edu*
