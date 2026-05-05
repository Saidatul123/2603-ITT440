


# 🖼️ Batch Image Processing System  
### Concurrent & Parallel Programming Project

---

## 📋 Student Information

| Field | Details |
|------|--------|
| Name | Al-hasan Bin Amran |
| Student ID | 2024943897 |
| Subject | ITT440 - Network Programming |
| Group | CS2554B |
| Date | May 2026 |

---

## 📌 Project Overview

This project implements a **Batch Image Processing System** that demonstrates the use of:

- Sequential Programming  
- Concurrent Programming (Threading)  
- Parallel Programming (Multiprocessing)  

The system processes a large number of images and compares execution performance between these approaches.

---

## 🎯 Objectives

- Process a large volume of image data efficiently  
- Compare execution time between different approaches  
- Demonstrate the use of concurrency and parallelism  
- Visualize performance using graphs  
- Provide a user-friendly GUI  

---

## 🛠️ Technologies Used

- Python 3.x  
- Tkinter (GUI)  
- Pillow (Image Processing)  
- `concurrent.futures` (Threading)  
- `multiprocessing` (Parallel Processing)  
- Matplotlib (Graph Visualization)  

---

## ⚙️ System Features

- 📁 Select input and output folders  
- 🧪 Generate large number of images automatically  
- ⚡ Process images using:
  - Sequential method  
  - Threading (concurrent)  
  - Multiprocessing (parallel)  
- 🧠 Detect CPU cores using `cpu_count()`  
- ⏱️ Measure execution time  
- 📊 Display performance graph  
- 🖥️ Responsive GUI (non-freezing)  

---

## 🧩 System Workflow

1. User selects input and output folder  
2. User generates images (optional)  
3. System processes images using:
   - Sequential  
   - Threading  
   - Multiprocessing  
4. Execution time is recorded  
5. Performance graph is displayed  

---

## 🧠 Concepts Applied

### 🔹 Sequential Processing
Processes tasks one by one.

```python
for img in images:
    process(img)
````

---

### 🔹 Concurrent Programming (Threading)

Executes multiple tasks concurrently.

```python
from concurrent.futures import ThreadPoolExecutor
```

* Efficient for I/O-bound tasks
* Limited by Python Global Interpreter Lock (GIL)

---

### 🔹 Parallel Programming (Multiprocessing)

Executes tasks using multiple CPU cores.

```python
from multiprocessing import Pool, cpu_count
```

* True parallel execution
* Suitable for CPU-bound tasks

---

## ⏱️ Performance Measurement

Execution time is measured using:

```python
start = time.time()
# processing
end = time.time()
```

---

## 📊 Sample Output

```
CPU Cores Used: 8

Processing 1000 images...

===== PERFORMANCE RESULT =====
Sequential Processing      : 25.40 seconds
Threading (Concurrent)    : 18.20 seconds
Multiprocessing (Parallel): 20.10 seconds
```

---

## 📈 Performance Analysis

In this experiment:

* Sequential processing is the slowest
* Threading performs faster
* Multiprocessing may not always be the fastest

### 🔍 Explanation

Although multiprocessing is theoretically faster, the results show that **threading performs better** due to:

* The task being **I/O-bound** (reading and saving images)
* Threading handles I/O efficiently
* Multiprocessing introduces overhead:

  * Process creation
  * Memory usage
  * Inter-process communication
* Windows uses **spawn method**, increasing overhead

---

## 📊 Graph Visualization

A bar chart is generated using matplotlib:

* X-axis → Processing method
* Y-axis → Execution time
* Lower bar → Faster performance

---

## 🖥️ GUI Implementation

The system uses Tkinter to provide:

* Folder selection
* Image generation
* Start processing button
* Real-time result display

---

## ⚠️ Challenges & Solutions

### ❌ GUI Freezing

**Problem:** GUI becomes unresponsive during processing
**Solution:** Use threading to run tasks in background

---

### ❌ Matplotlib Thread Issue

**Problem:**

```
Matplotlib GUI outside main thread warning
```

**Solution:**

```python
root.after(0, lambda: show_graph(...))
```

---

### ❌ Image Overwriting

**Problem:** Generated images overwrite existing ones
**Solution:** Continue filename numbering dynamically

---

## 📂 Project Structure

```
project/
│
├── input_images/
├── output_images/
├── main.py
└── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install pillow matplotlib
```

---

### 2. Run the program

```
python main.py
```

---

### 3. Steps

1. Select input folder
2. Generate images
3. Select output folder
4. Click "Start Processing"

---

## 📌 Notes

* Recommended dataset size: **1000–5000 images**
* Avoid extremely large datasets (e.g. millions)
* Performance depends on task type (I/O vs CPU-bound)

---

## 🧠 Conclusion

* Sequential processing is the slowest
* Threading performs well for I/O-bound tasks
* Multiprocessing is best for CPU-intensive tasks

This project demonstrates that **performance depends on the nature of the task**, not just the method used.

---
## 🎥 Demo Video

Watch the full demonstration here:  
https://youtu.be/bXaaAB_mEqQ
