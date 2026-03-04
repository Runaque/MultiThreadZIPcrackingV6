# HPC Zip Cracker V6: Devil's Edition 😈

A high-performance, multi-threaded ZIP password recovery tool optimized for high-RAM environments and multi-core architectures. This script utilizes a parallel processing "Gatling gun" approach to bypass the Python Global Interpreter Lock (GIL).


<img width="1140" height="659" alt="image" src="https://github.com/user-attachments/assets/211f508f-5de6-4e6f-82a2-0042acdbf11e" />


## 🚀 Performance Metrics
* **Devil Edition (V6):** ~2028 pwd/s (Optimized thread rotation)
* **Visuals:** Features a menacing **Red** progress bar and **Hacker Green** success terminal.

## 📦 Requirements
Install the necessary dependencies before running:
```bash
pip install pyzipper tqdm
````
# 📖 Usage
Run the script from your terminal:

````Bash
py MultiThreadZIPcrackingV6.py -z zip-file_here.zip -d wordlist_here.txt
````
Advanced Flags
-c: Manual core count (e.g., -c 8 for the i7-12700H sweet spot).

-o: Output folder for successful extractions (Default: .\extracted_output).

# ⚠️ Thermal & Hardware Warning
This tool is designed to saturate CPU resources.

Tested Thermal: 92°C (Monitor your fans and CPU clock speeds!)

Recommended RAM: 64GB for wordlists exceeding 5GB to ensure zero-latency memory loading.

# ⚖️ License
This project is licensed under the MIT License.

# 🔒 Hash

MD5 hash: fdbb47a03a21fc00d809cba06c3494b8

SHA1 hash: 4b8fed7874fec1358cddab123256cb4adc325829

SHA256 hash: 10efd4207ea2fc17477861628d7f6c0d9b4faa69623724dcf449d56c91a57f71

SHA512 hash: 2730dfbc10c269f3f8e6d8dc9ac608da1cfa8963ef0550b683b291bc70a650cfe608fc7f2b4eeecb537c7dc0fe2900771312ac508f9148453264bea8a5e50b91


