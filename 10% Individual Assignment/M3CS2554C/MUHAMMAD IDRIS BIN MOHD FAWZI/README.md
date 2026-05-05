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

```text
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

- Process a **large volume of data** (up to 100,000 QR codes) efficiently.  
- Use **parallel programming** (`multiprocessing`) for CPU‑intensive QR generation.  
- Use **concurrent programming** (`threading`) for I/O‑intensive QR decoding.  
- Compare sequential, concurrent, and parallel execution times to **prove performance gains**.  
- Deliver a clean, well‑documented, and reproducible GitHub repository.

---

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| **Operating System** | Windows, Linux, or macOS |
| **Python** | 3.8 or newer |
| **Python libraries** | `qrcode`, `Pillow`, `pyzbar`, `opencv-python` |
| **System library** | `zbar` (needed for decoding) |

### 🔧 Installing `zbar`
- **Windows:** Download `libzbar-64.dll` from [pyzbar releases](https://github.com/NaturalHistoryMuseum/pyzbar/releases) and place it in the project folder (example: `C:\Windows\System32`).  
- **Linux:** `sudo apt install libzbar0`  

---

## 📥 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/parallel-qr-generator-decoder.git
cd parallel-qr-generator-decoder

# 2. Create & activate a virtual environment (recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

🚀 How to Run
The program uses an interactive command‑line interface. Just start it and follow the prompts:

bash
python main.py
📋 Step‑by‑step execution
Enter the number of QR codes you want to generate (e.g., 10000).

Choose generation mode – s for sequential, p for parallel (default).
If parallel, you can set the number of worker processes (default: 4).

Press Enter to start generation; all QR images are saved in the qr_output/ folder.

After generation, the program asks you to press Enter to begin decoding.

Choose decoding mode – s for sequential, t for threaded (default).
Thread count can be adjusted (default: 8).

The program decodes every image and prints the success rate and a performance summary.
