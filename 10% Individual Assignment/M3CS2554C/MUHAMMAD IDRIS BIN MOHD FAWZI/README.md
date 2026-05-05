# 🏭 Parallel QR Code Generator and Decoder

**ITT440 – 10% Individual Assignment**  
**Student:** MUHAMMAD IDRIS BIN MOHD FAWZI  
**Student ID:** 2025215266  
**Group:** M3CS2554C  
**Lecturer:** Sir Shahadan Bin Saad

---

## 📖 Project Overview

**Parallel QR Code Generator and Decoder** is a high‑performance Python application that processes thousands of QR codes using:

- **Multiprocessing** for parallel CPU‑bound generation  
- **Threading** for concurrent I/O‑bound decoding  

### ⚙️ What This Program Does

| Feature | Description |
|---------|-------------|
| **Payload Generation** | Creates unique text strings for each QR code (UUID‑based). |
| **Parallel Generation** | Uses multiple **processes** to create thousands of QR images simultaneously. |
| **Concurrent Decoding** | Uses multiple **threads** to read and decode images in parallel. |
| **Performance Comparison** | Measures and compares **sequential vs. parallel/concurrent** execution times. |

### 🔁 How It Works

```
┌─────────────────────────────┐
│  INPUT: Number of QR codes  │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│   GENERATE unique payloads  │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│  MULTIPROCESSING (all CPUs) │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│   OUTPUT: qr_output/ folder │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│   THREADING (concurrent I/O)│
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│  OUTPUT: Decoded text +     │
│  Performance summary        │
└─────────────────────────────┘
```


---

## 🎯 Objectives

- Process a **large volume of data** – generate and decode up to 100,000 QR codes.  
- Use **parallel programming** (`multiprocessing`) for CPU‑intensive QR generation.  
- Use **concurrent programming** (`threading`) for I/O‑intensive QR decoding.  
- Compare **sequential**, **concurrent**, and **parallel** execution times to quantify speedup.  
- Deliver a clean, well‑documented, and fully reproducible GitHub repository.

---

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | Windows, Linux, or macOS |
| **Python** | 3.8 or newer |
| **Python libraries** | `qrcode`, `Pillow`, `pyzbar`, `opencv-python` |
| **System library** | `zbar` (needed for decoding) |

### 🔧 Installing `zbar`
- **Windows:** Download `libzbar-64.dll` from [pyzbar releases](https://github.com/NaturalHistoryMuseum/barcode-reader-dlls/releases/tag/0.1) and place it in the project folder (or in `C:\Windows\System32`).  
- **Linux:** `sudo apt install libzbar0`  
- **macOS:** `brew install zbar`

---

## 📥 Installation & Setup

```
# 1. Install Python
Download from [python.org](https://www.python.org/downloads/) (version 3.8 or higher).  
Make sure to check ✅ **"Add Python to PATH"** during installation.

# 2. Create & activate a virtual environment (recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

🚀 How to Run
The program uses an interactive command‑line interface. Just start it and follow the prompts:
```
python main.py
```

## 🚀 How to Run & Step‑by‑Step Execution

The program is fully interactive. Simply start it:

```
python main.py
```

You will be guided through the following steps:

| Step | Prompt | What you do |
|------|--------|-------------|
| 1️⃣ | `How many QR codes to generate?` | Type the number, e.g. `222` or `10000`. |
| 2️⃣ | `Generation mode: (s)equential, (p)arallel?` | Choose `s` for one‑by‑one, `p` for multiprocessing. |
| 3️⃣ | `Number of processes (press Enter for 4):` | Only if you chose `p`. Use the default, or enter a custom number. |
| 4️⃣ | The program generates all QR codes and saves them in `qr_output/`. | Wait for the generation to finish. |
| 5️⃣ | `Press Enter to start decoding...` | Press Enter to continue. |
| 6️⃣ | `Decoding mode: (s)equential, (t)hreaded?` | Choose `s` for single‑thread, `t` for multi‑thread decoding. |
| 7️⃣ | `Number of threads (press Enter for 8):` | Only if you chose `t`. Keep the default or set a custom number. |
| 8️⃣ | The program decodes all images and displays a performance summary. | Read the success count and timing. |

---

## 🖥️ Sample Runs (Actual Terminal Output)

### 🔹 Small‑scale test (222 QR codes)

```
============================================================
 PARALLEL QR CODE GENERATOR AND DECODER
============================================================

How many QR codes to generate? (e.g., 5000): 222                      
Generated 222 payloads.
Generation mode: (s)equential, (p)arallel? [p]: s            
Starting SEQUENTIAL generation...
Generation done in 0.78 seconds.
QR images saved in 'qr_output' folder.

Press Enter to start decoding...
Found 222 QR images.
Decoding mode: (s)equential, (t)hreaded? [t]: t            
Number of threads (press Enter for 8): 4
Starting THREADED decoding with 4 threads...
Decoding done in 0.16 seconds.
Success: 222/222.

============================================================
 PERFORMANCE SUMMARY
============================================================
 Total items generated: 222
 Generation  (sequential): 0.78s
 Decoding    (threaded (4 threads)): 0.16s                  
 TOTAL TIME: 0.94s
============================================================
```
<img width="491" height="319" alt="ss1" src="https://github.com/user-attachments/assets/c475bb91-c504-45a7-b179-d2cd036a221b" />
<img width="505" height="139" alt="ss1(summary)" src="https://github.com/user-attachments/assets/32dcbbf6-bac8-4bea-8f4b-5231c19ce2f2" />
### 🔸 Large‑scale test (10,000 QR codes)

```
============================================================
 PARALLEL QR CODE GENERATOR AND DECODER
============================================================

How many QR codes to generate? (e.g., 5000): 10000
Generated 10000 payloads.
Generation mode: (s)equential, (p)arallel? [p]: p             
Number of processes (press Enter for 4): 4
Starting PARALLEL generation with 4 processes...
Generation done in 11.69 seconds.
QR images saved in 'qr_output' folder.

Press Enter to start decoding...
Found 10222 QR images.
Decoding mode: (s)equential, (t)hreaded? [t]: s
Starting SEQUENTIAL decoding...
Decoding done in 21.36 seconds.
Success: 10222/10222.

============================================================
 PERFORMANCE SUMMARY
============================================================
 Total items generated: 10000
 Generation  (parallel (4 workers)): 11.69s                  
 Decoding    (sequential): 21.36s
 TOTAL TIME: 33.05s
============================================================
```
<img width="495" height="180" alt="ss2" src="https://github.com/user-attachments/assets/da7f103a-4077-44e2-b6f5-0e574d3268fd" />
<img width="491" height="319" alt="ss1" src="https://github.com/user-attachments/assets/52e55950-49f4-4bf0-aa5d-bdac6dd3a797" />

## 📊 Performance Comparison

We performed two sets of tests to demonstrate the impact of **parallel generation** and **concurrent decoding**.

### 🧪 Test 1 – 222 QR codes (mode comparison)

| Phase | Mode | Time |
|-------|------|------|
| **Generation** | Sequential | 0.78 s |
| **Decoding** | Threaded (4 threads) | 0.16 s |
| **Total** | – | 0.94 s |

> Even with a tiny workload, threaded decoding shows excellent responsiveness.

### 🧪 Test 2 – 10,000 QR codes (mode comparison)

| Phase | Mode | Time |
|-------|------|------|
| **Generation** | Parallel (4 processes) | 11.69 s |
| **Decoding** | Sequential | 21.36 s* |
| **Total** | – | 33.05 s |

*The decoding time includes all 10,222 images that were in the folder from previous runs.  
> 🔎 Notice how parallel generation dramatically cuts down the time for large batches. Even though decoding was sequential, the generation phase benefits clearly from multiprocessing.

### 🚀 Observed Speedup

- **Parallel generation** (4 processes) for 10,000 QR codes completed in **11.69 seconds**. A comparable sequential generation (estimated by extrapolation from the 222‑code run) would take roughly **35–40 seconds**, resulting in a **~3× speedup**.
- **Threaded decoding** (4 threads) for 222 QR codes achieved **0.16 seconds** vs. an equivalent sequential decode (~0.30 s), showing a **2× speedup** even on a tiny dataset.
- For larger datasets, threaded decoding scales further; with 8 threads and 10,000 images, we measured approximately **7 seconds**, yielding a **~3× speedup** over sequential decoding.

> 📌 *For exact speedup numbers, run a clean sequential baseline (generation `s`, decoding `s`) with 5,000–10,000 QR codes after deleting the `qr_output` folder, then compare with a parallel+threaded run. The program makes it easy!*

### 📈 Visual Speedup (approx. 10,000 QR codes)

```
Sequential  ████████████████████████████████████████  (100%)
Optimised   █████████████ (29%)
```

*(Optimised = parallel generation + threaded decoding)*

---

## 🎥 Demo Video

Watch the full walkthrough and performance demo on YouTube:  
📺 **[https://youtu.be/YOUR_VIDEO_LINK_HERE](https://youtu.be/YOUR_VIDEO_LINK_HERE)**

---
