# MUHAMMAD NUAIM NUKMAN BIN RUSLI
# PARALLEL BANK TRANSACTION FRAUD DETECTION
# 🏦 Parallel Bank Transaction Fraud Detector: Using Parallel Computing to Detect Financial Threats

**Course Code:** ITT440: Network Programming
**Lecturer:** Shahadan Bin Saad
**Youtube link :** https://youtu.be/QKEtepbAv8s

---

## 🛡️ 1. Mission Objective

In modern banking, **Speed = Security**. Processing 10 million transactions using traditional, single-core methods is a bottleneck that leaves financial systems vulnerable to undetected fraud.

The **Parallel Bank Transaction Fraud Detector** is a high-performance engine that utilizes **Parallel Computing** to analyze massive transaction datasets in real time. By distributing the workload across all available CPU cores, it transforms an ordinary laptop into a fraud detection powerhouse — flagging suspicious transactions in a fraction of the time.

---

## 💻 2. Hardware & Environment

1. **Processor:** Quad-Core / Octa-Core CPU
2. **Memory:** 8GB RAM minimum
3. **OS:** Linux Environment (Ubuntu 22.04+ recommended)
4. **Runtime:** Python 3.8+ with `matplotlib` for analytics and `tqdm` for real-time progress

---

## ⚠️ Disclaimer

> The 10,000,000 transaction log file is **not included** in this GitHub repository due to size constraints. It is generated automatically at runtime.

---

## 🔧 3. Deployment Guide

### A. System Ignition

**Create a new project folder:**
```bash
mkdir ITT440_FraudDetector
cd ITT440_FraudDetector
```

**Initialize a virtual environment in the `venv` directory:**
```bash
python3 -m venv venv
```

**Standard activation command for Linux/macOS:**
```bash
source venv/bin/activate
```

**Install tqdm (Real-time progress bars):**
```bash
pip install tqdm
```

**Install Matplotlib (Automatic performance graph generation):**
```bash
pip install matplotlib
```

---

### B. Engagement Protocol

To launch the analysis, execute the main engine:

**Activate Venv:**
```bash
source venv/bin/activate
```

**Run Program:**
```bash
python3 analyzer.py
```

---

## 📊 4. Battlefield Analytics

### A. 10 Million Transactions

When the analyzer completes its scan, it generates a comprehensive **Fraud Detection Report**. Here is what a typical high-stress test looks like:

| Fraud Type | Detection Count |
|---|---|
| `LARGE_AMOUNT_FLAG` | varies |
| `RAPID_TRANSACTION_FLAG` | varies |
| `BLACKLISTED_ACCOUNT` | varies |
| `SUSPICIOUS_INTERNATIONAL` | varies |
| **Total Fraud Detected** | **reported at runtime** |

> Full results are saved to `fraud_detection_results.txt`

---

### B. Performance Benchmark (10M Transactions)

| Method | Time |
|---|---|
| Sequential (1 Core) | ~36s |
| Concurrent | ~2.9s |
| Parallel (8 Cores) | ~11s |
| **Performance Gain** | **🚀 ~3x Faster (Parallel vs Sequential)** |

```
ITT440 Performance Benchmark: Fraud Detection
Data Size: 10,000,000 Transactions
```

![Performance Chart](performance_result.png)

---

## 🧠 5. How It Works (The Logic)

The engine doesn't just work harder; it works **smarter** by using a **MapReduce Pattern**.

1. **Partition (Map):** The 10 million transactions are sliced into equal chunks — one per CPU core.
2. **Analyze:** Each CPU core receives a chunk and runs high-speed fraud rule matching **simultaneously**.
3. **Synthesize (Reduce):** The engine pulls results from all cores together to produce the **final fraud tally**.

---

## 🗂️ 6. Project Structure

```
ITT440_FraudDetector/
├── analyzer.py               # Main engine (sequential + concurrent + parallel)
├── fraud_detection_results.txt  # Output: all 10M transaction records
├── performance_result.png    # Auto-generated benchmark chart
├── venv/                     # Python virtual environment
└── README.md
```

---

## ✅ 7. Final Verdict

The **Parallel Bank Transaction Fraud Detector** proves that **parallel computing** is the gold standard for modern financial security.

By cutting analysis time by over **70%**, we ensure that bank security teams can respond to fraudulent activity in **real-time** rather than hours after the damage is done.

---

**Status: Mission Accomplished. System Optimized. 🚀**


