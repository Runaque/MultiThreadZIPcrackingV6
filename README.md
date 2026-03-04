# MultiThreadZIPcrackingV6


# HPC Zip Cracker V6: Devil's Edition 😈

A high-performance, multi-threaded ZIP password recovery tool. This script is designed to bypass the Global Interpreter Lock (GIL) and saturate CPU resources for maximum throughput.

## 🚀 Performance Metrics
* **Devil Edition (V6):** ~2028 pwd/s (Optimized thread rotation)
* **Visuals:** Features a menacing **Red** progress bar and **Hacker Green** success terminal.

## 📦 Requirements
Install the necessary "ammunition" for the Gatling gun:
```bash
pip install pyzipper tqdm

📖 Usage
Run the script from your terminal:

Bash
python MultiThreadZIPcrackingV6.py -z protected.zip -d wordlist.txt
Advanced Flags:
-c: Manual core count (e.g., -c 8 for the Acer Nitro sweet spot).

-o: Output folder for successful extractions (Default: .\extracted_output).

⚠️ Thermal & Hardware Warning
This tool is designed for high-performance hardware.

Tested Thermal: 92°C (Monitor your fans and CPU clock speeds!)

Recommended RAM: 64GB for wordlists >5GB to ensure zero-latency memory loading.

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
