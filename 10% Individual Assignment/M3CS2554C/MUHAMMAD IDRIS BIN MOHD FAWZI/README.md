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

INPUT: Number of QR codes (e.g., 10,000)
│
▼
[GENERATE] Unique payloads (text strings)
│
▼
[MULTIPROCESSING] Create QR codes using all CPU cores
│
▼
OUTPUT: qr_output/ (thousands of .png images)
│
▼
[THREADING] Decode images using multiple threads
│
▼
OUTPUT:
• Decoded text data (displayed on screen)
• Performance summary (time & speedup)
