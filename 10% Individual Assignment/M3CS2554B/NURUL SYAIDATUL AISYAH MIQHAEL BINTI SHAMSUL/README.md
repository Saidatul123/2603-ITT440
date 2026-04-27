# 🎬 Movie Recommendation Analyzer: A High-Performance Implementation Using Python

---

## 📌 Introduction
This system focuses on the performance differences between Sequential, Concurrent, and Parallel programming models using Python. By processing a large dataset of 3,000,000 movie ratings, the system shows how using multiple CPU cores can significantly reduce execution time, especially for tasks that require heavy computation.

---

## ❗ Problem Statement

Processing large datasets using sequential execution is time-consuming and inefficient, especially with modern multi-core processors.

Although concurrency using threading allows multiple tasks to run at the same time, it is limited by the Global Interpreter Lock (GIL) in Python because it cannot fully use multiple CPU cores for heavy calculations.

Therefore, this system aims to:
- Identify the performance limitations of sequential and concurrent methods  
- Measure the performance improvement when using multiprocessing  
- Determine the speedup achieved when distributing workload across multiple CPU cores  

---

## ⚙️ System Requirements

To ensure the system runs smoothly, the following requirements were met:

| Component           | Details |
|---------------------|--------|
| Software            | Python 3.14 |
| Libraries           | multiprocessing, threading, collections, statistics, time, matplotlib |
| Development Tool    | VS Code (Visual Studio Code) |
| Operating System    | Windows (Local Environment) |
| Hardware            | Multi-core processor (12 cores) |

---

## 🛠️ Installation Steps

### Step 1: Install Python
Ensure Python 3.14 is installed on your system.

### Step 2: Install Required Library
Run the following command in terminal:

```bash
python3.14 -m pip install matplotlib --break-system-packages
```
### Step 3: Setup Project Directory
Ensure all source files are placed in the same project folder, for example:

Documents/ITT440/Movie Recommendation Analyzer

## ▶️ How To Run

### Step 1: Open Project Folder
Launch VS Code and open the project directory:
`Documents/ITT440/Movie Recommendation Analyzer`

---

### Step 2: Open Terminal
Open the terminal in VS Code.  
Make sure the terminal path is the same as your project folder.

---

### Step 3: Run the Program
Enter the following command:

```bash
python3.14 source_code.py
```

### Step 4: Monitor Process Generation
Observe the terminal as the system generates **3,000,000 records** and saves them into `input.txt`.

---

### Step 5: Verify Concurrent Responsiveness
Look for the **"Ping" messages** from the concurrent UI thread.  
These messages show that the system remains responsive even while processing heavy data.

---

### Step 6: View Final Performance Results
Once the analysis is complete:
- The terminal will display the **Final Performance Benchmark results**
- The file `output.txt` will be generated
- A pop-up window will appear showing the **Benchmark Results chart**

## 📊 Sample Input / Output

### 🖥️ Terminal Output
The system displays the time taken for each mode:

<img width="1456" height="766" alt="terminal" src="https://github.com/user-attachments/assets/6ace80db-8f0b-4e3c-949c-cb030e315d7f" />
<p align="center"><i>Figure 1.1 Terminal Output</i></p>

- Sequential: ~136.4758s  
- Concurrent: ~29.1252s  
- Parallel: ~28.3052s
- Speedup Ratio between Parallel and Sequential: ~4.82x Faster 

---

### 📄 Input File (`input.txt`)
Contains 3,000,000 generated movie rating records including:
- Movie title  
- Rating  

<img width="628" height="482" alt="input" src="https://github.com/user-attachments/assets/e861d44e-0587-42d1-a6af-420bcd490a49" />
<p align="center"><i>Figure 1.2 input.txt</i></p>

---

### 📄 Output File (`output.txt`)
Contains:
- Top 100 ranked movies  
- Genre classification  
- Average rating scores 

<img width="620" height="481" alt="output" src="https://github.com/user-attachments/assets/476426a3-aa30-4fb7-b49f-e07eb4adc548" />
<p align="center"><i>Figure 1.3 output.txt</i></p>

 
---

### 📈 Visual Output
A bar chart titled:

**"Performance Comparison: Processing 3,000,000 Records"**

Saved as `BenchmarkResults.png

<img width="1000" height="600" alt="BenchmarkResults" src="https://github.com/user-attachments/assets/0065db90-7797-439d-a2c1-7745779bf525" />
<p align="center"><i>Figure 1.4 Benchmark Results.txt</i></p>

## 💻 Source Code

The system is implemented in Python and includes:

- Data generation for large-scale dataset  
- Sequential processing  
- Concurrent threading (UI responsiveness)  
- Parallel multiprocessing (multi-core execution)  
- Data aggregation and ranking  
- Performance visualization using matplotlib  

<img width="1737" height="1005" alt="sc1" src="https://github.com/user-attachments/assets/0d50d551-7e5c-4097-81d8-9c6383f5654e" />
<img width="1737" height="1009" alt="sc2" src="https://github.com/user-attachments/assets/cd015244-4d6c-42cf-b897-58e4fd8e78de" />
<img width="1738" height="1004" alt="sc3" src="https://github.com/user-attachments/assets/b000b1f1-f0eb-4114-bd04-378c785a6acf" />
<img width="1736" height="1006" alt="sc4" src="https://github.com/user-attachments/assets/568ddfe5-eede-480e-a3e0-62d2e34c2154" />
<img width="1739" height="1003" alt="sc5" src="https://github.com/user-attachments/assets/04af9dbb-75f6-44aa-9f34-d8d2c020d619" />
<img width="1736" height="1009" alt="sc6" src="https://github.com/user-attachments/assets/0953a609-31d7-4837-a280-0f72b906b392" />
<img width="1740" height="1004" alt="sc7" src="https://github.com/user-attachments/assets/e99324aa-267a-4ae9-9004-8d6d846b5b00" />

---

## ✅ Conclusion

The results show that parallel programming is the most efficient approach for processing large datasets.

Sequential execution required over 136 seconds, while the parallel method reduced execution time to approximately 28 seconds by using all available CPU cores.

Although threading improves system responsiveness, it does not significantly improve performance for heavy calculations due to Python’s GIL. Therefore, multiprocessing is the most suitable method to achieve better performance when handling large amounts of data.



