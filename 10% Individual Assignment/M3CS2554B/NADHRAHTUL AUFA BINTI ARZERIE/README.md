# NADHRAHTUL AUFA BINTI ARZERIE
# Task Queue Simulator
# CLASS : M3CS2554B
# ITT440

# INTRODUCTION 
The Task Queue Simulator is a performance benchmarking application developed to analyze the efficiency of various computational models in handling high-volume task queues. In computing, a task queue is a mechanism used to manage asynchronous work units that need to be processed. This project simulates a scenario where 500 tasks (simulating user requests) are pushed into a queue and processed using three distinct methods: Sequential, Threading, and Multiprocessing. The goal is to determine the optimal execution model for handling CPU-intensive workloads without causing system bottlenecks.

# OBJECTIVES
1) To Evaluate Execution Models: To compare how Sequential, Threading, and Multiprocessing models manage a workload of 500 simulated tasks.
2) To Benchmark Latency: To measure and record the total execution time (latency) for each processing technique to identify the most time-efficient method.
3) To Demonstrate Resource Utilization: To observe how utilizing multiple CPU cores (Parallelism) through the Multiprocessing library improves system throughput.
4) To Provide Data Visualization: To generate real-time progress updates and a final performance comparison chart for empirical analysis.

# SYSTEM REQUIREMENTS
1) Hardware Requirements
To achieve accurate benchmarking results, especially for parallel processing, the following hardware is used:
- Processor: Multi-core CPU (e.g., Intel Core i5/i7 or AMD Ryzen 5/7) to allow true parallel execution.
- RAM: Minimum 8GB to support multiple sub-processes running simultaneously.
- System Type: 64-bit Operating System.

2) Software Requirements
- The environment used to develop and execute the simulator includes:
- Operating System: Windows 10/11.
- Programming Language: Python 3.10+ (Selected for its robust multiprocessing and threading libraries).
- IDE: Visual Studio Code (VS Code).

Key Libraries:
- tqdm: Used for real-time task queue progress visualization.
- matplotlib: Used for generating the final performance bar chart.
- time & multiprocessing: Core modules for measuring execution and managing process pools.

# CODING IN PYTHON
``` python
import threading
import multiprocessing
import time
from tqdm import tqdm

def process_registration(student_id):
    count = 0
    for i in range(10**6): 
        count += i

def run_sequential(num):
    print(f"\n[*] Running Sequential Mode...")
    start = time.time()
    for i in tqdm(range(num), desc="Progress"):
        process_registration(i)
    return time.time() - start

def run_threading(num):
    print(f"\n[*] Running Threading Mode...")
    start = time.time()
    threads = [threading.Thread(target=process_registration, args=(i,)) for i in range(num)]
    for t in threads: t.start()
    for t in tqdm(threads, desc="Progress"): t.join()
    return time.time() - start

def run_multiprocessing(num):
    print(f"\n[*] Running Multiprocessing Mode...")
    start = time.time()
    with multiprocessing.Pool() as pool:
        list(tqdm(pool.imap(process_registration, range(num)), total=num, desc="Progress"))
    return time.time() - start

if __name__ == "__main__":
    TOTAL = 500
    
    t1 = run_sequential(TOTAL)
    t2 = run_threading(TOTAL)
    t3 = run_multiprocessing(TOTAL)
    
    print("\n\n" + "╔" + "═"*58 + "╗")
    print(f"║ {'TASK QUEUE SIMULATOR REPORT':^56} ║")
    print("╠" + "═"*28 + "╦" + "═"*29 + "╣")
    print(f"║ {'EXECUTION METHOD':<26} ║ {'TIME CONSUMED (s)':^27} ║")
    print("╠" + "═"*28 + "╬" + "═"*29 + "╣")
    print(f"║ 1. Sequential (Legacy)     ║ {t1:>23.4f}s ║")
    print(f"║ 2. Threading (Concurrent)  ║ {t2:>23.4f}s ║")
    print(f"║ 3. Multiprocessing (Parallel)║ {t3:>23.4f}s ║")
    print("╚" + "═"*28 + "╩" + "═"*29 + "╝")
    
    improvement = ((t1 - t3) / t1) * 100
    print(f"\n[ RESULT ] Multiprocessing is {improvement:.1f}% faster than Sequential.")
    print("[ STATUS ] System is optimized for High-Traffic Registration.\n")

    try:
        import matplotlib.pyplot as plt

        print("[*] Generating Chart...")
        methods = ['Sequential', 'Threading', 'Multiprocessing']
        times = [t1, t2, t3]
        colors = ['#e74c3c', '#3498db', '#2ecc71'] # Merah, Biru, Hijau

        plt.figure(figsize=(9, 6))
        bars = plt.bar(methods, times, color=colors, edgecolor='black', linewidth=1.2)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f'{yval:.3f}s', 
                     ha='center', va='bottom', fontweight='bold', fontsize=11)

        plt.ylabel('Execution Time (Seconds)', fontweight='bold')
        plt.title(f'Task Queue Simulator', fontsize=14, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        plt.savefig('ufuture_chart_result.png')
        print("[✔] Chart saved as 'ufuture_chart_result.png'")
        
        plt.show()

    except ImportError:
        print("\n[!] Matplotlib not found. Please run 'pip install matplotlib' to enable the Charting function.")
    except Exception as e:
        print(f"\n[!] fail to execute chart: {e}")
```

# OUTPUT 
<img width="1620" height="561" alt="Screenshot 2026-04-23 235259" src="https://github.com/user-attachments/assets/b99ca40e-ee44-4c73-a70a-ffc65aa4b6f4" />
- OUTPUT IN TERMINAL

<img width="1129" height="831" alt="Screenshot 2026-04-23 234334" src="https://github.com/user-attachments/assets/7ab6df97-fd4e-48af-af80-5da2583f3471" />
- OUTPUT BAR CHART BETWEEN SEQUENTIAL, THREADING AND MULTIPROCESSING

# RESULT & PERFORMANCE ANALYSIS
This section presents the benchmarking results for the processing of 500 simulated tasks. Based on the data obtained, the Sequential method was identified as the least efficient, with an execution time of 12.5 seconds. Although Threading was implemented, it showed minimal concurrency gains due to system overhead.

In contrast, the generated performance chart highlights Multiprocessing as the superior execution model. By leveraging parallel CPU cores, it successfully reduced the execution time to only 3.67 seconds. This approach provides a substantial 70.7% speed improvement, effectively validating the optimization strategy for the Task Queue Simulator.

# DEMONSTRATION VIDEO
https://youtu.be/yOzKTtNXVW0
