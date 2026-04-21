# Password Generator and Analysis System
#### Student Name: NUR SHAHAINA BINTI MAT RASHID
#### Student ID: 2024421182
#### Group: M3CS2554B


## 1. Introduction

This project is about developing a simple password generator using Python. The program can generate a large number of passwords and check their strength. The strength is divided into three levels which are Weak, Medium, and Strong.

In this project, I also applied different programming techniques which are sequential, threading, and multiprocessing. The purpose is to understand how these methods work and compare their performance.

---

## 2. Problem Statement

When a program needs to process many tasks, doing everything one by one can be slow. In real systems, we can use concurrency and parallel programming to improve performance.

Therefore, this project is created to simulate how multiple tasks can be processed using different approaches in Python.

---

## 3. Objectives

The objectives of this project are:

- To develop a password generator using Python  
- To classify password strength into Weak, Medium, and Strong  
- To implement threading as a concurrent programming technique  
- To implement multiprocessing as a parallel programming technique  
- To compare the execution time between different methods  

---

## 4. Methodology

### Sequential Method
In this method, the program generates passwords one by one. It is simple but may be slower when the number of tasks is large.

### Threading Method
Threading allows multiple tasks to run at the same time. In this project, threads are used to generate passwords concurrently.

### Multiprocessing Method
Multiprocessing creates multiple processes that can run in parallel using CPU cores. This method is used to test parallel execution.

---

## 5. System Description

The program works as follows:

1. The user enters the number of passwords to generate  
2. The system generates passwords using sequential method  
3. The system generates passwords using threading (concurrent) 
4. The system generates passwords using multiprocessing (parallel) 
5. The system displays the results and compares execution time  

Each generated password is also checked to determine whether it is Weak, Medium, or Strong.

---

## 6. USER MANUAL

### 6.1 System Requirements

- Python 3.x  
- Visual Studio Code (or any Python IDE)  
- Operating System: Windows / Mac / Linux  

---

### 6.2 Installation Steps

1. Install Python from https://www.python.org  
2. Install Visual Studio Code  
3. Download or clone the project from GitHub  
4. Open the project folder in VS Code 

---

### 6.3 How to Run the Program

Open terminal in VS Code and run:
python main.py

---

## 7. Sample Output
<img width="675" height="978" alt="image" src="https://github.com/user-attachments/assets/f5e8747f-65a2-4512-859b-3d005715d079" />

---

## 8. Discussion

This project successfully demonstrates:

- Concurrent programming using threading  
- Parallel programming using multiprocessing  
- Processing of a large number of tasks  
- Performance comparison between different approaches  

Even though multiprocessing is not always faster in this case, it still shows how parallel programming works.

---

## 9. Links  
YouTube Demo: (paste your video link)
