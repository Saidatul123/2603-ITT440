# 📈 CUSTOMER FEEDBACK ANALYZER
NAME: SITI NURUL NAJWA BINTI NORDIN <br>
STUDENT ID: 2024423364
# USER MANUAL & TECHNICAL DOCUMENTATION
Welcome to the Customer Feedback Analyzer. This tool is designed to process large-scale customer feedback data and provides a performance benchmarking suite to analyze how different Python concurrency models (Sequential, Threading, and Multiprocessing) handle CPU-bound workloads.
# SYSTEM REQUIREMENTS
* **Python Version:** 3.8 or higher
* **Operating System:** Windows, macOS, or Linux
* **Dependencies:**
    * **tkinter** (Standard Python library)
    * **matplotlib** (For data visualization)
    * **multiprocessing** (Standard library)
    * **threading** (Standard library)
# 📥 Installation Steps
1. **Clone or Download:** git clone https://github.com/kiddygo1up/gui_analyzer.git <br>
cd gui_analyzer
2. **Install Dependencies:** Ensure matpotlib is installed in your environment <br> pip install matpotlib <br>
# 🚀 How to Run 
Once installed, execute the script from your terminal: python main.py <br> 
# 📖 User Manual
The application is divided into three distinct stages: <br> <br>
**Step 1: Data Management**
* **Generate Test Data:** Creates 1,000 synthetic feedback entries across three categories (Short, Detailed, Enterprise). <br> This is recommended for first-time users.
* **Browse for File:** Import your own .txt file. Each line in the file will be treated as an individual feedback entry.
* **Dropdown Selection:** Switch between data categories to observe how analysis time scales with text length. <br> <br>
**Step 2: Benchmarking**
* **Sequential (Baseline):** Runs the analysis on the main thread. Best for verifying accuracy before scaling.
* **Threading (GIL-Limited):** Attempts parallel execution. Note: You will likely observe slower performance than Sequential due to the Global Interpreter Lock (GIL).
* **Multiprocessing (True Parallel):** The performance mode. It spawns independent processes for every CPU core. This will be the fastest method for large datasets. <br> <br>
**Step 3: Export**
* **Export to CSV:** Save the calculated "Analysis Scores" and a snippet of the feedback to a CSV file for your reporting needs. <br> 
# 📝 Sample Input & Output 
**Input**  <br>
The application expects a .txt file where each line is a single feedback string. <br>
User are expected to run the "Generate Test Data" option before using .txt files. <br> <br>
**Output** <br>
picture
# 🖼️ Screenshots
Below is the GUI for feedback analyzer: <br>


