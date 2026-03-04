Markdown
# HPC Zip Cracker V6: Devil's Edition 😈

A high-performance, multi-threaded ZIP password recovery tool optimized for high-RAM environments and multi-core architectures. This script utilizes a parallel processing "Gatling gun" approach to bypass the Python Global Interpreter Lock (GIL).

## 🚀 Performance Metrics
* **Devil Edition (V6):** ~2028 pwd/s (Optimized thread rotation)
* **Visuals:** Features a menacing **Red** progress bar and **Hacker Green** success terminal.

## 📦 Requirements
Install the necessary dependencies before running:
```bash
pip install pyzipper tqdm

Markdown
# 📖 Usage
Run the script from your terminal:

Bash
python MultiThreadZIPcrackingV6.py -z protected.zip -d wordlist.txt
Advanced Flags
-c: Manual core count (e.g., -c 8 for the i7-12700H sweet spot).

-o: Output folder for successful extractions (Default: .\extracted_output).

⚠️ Thermal & Hardware Warning
This tool is designed to saturate CPU resources.

Tested Thermal: 92°C (Monitor your fans and CPU clock speeds!)

Recommended RAM: 64GB for wordlists exceeding 5GB to ensure zero-latency memory loading.

⚖️ License
This project is licensed under the MIT License.
