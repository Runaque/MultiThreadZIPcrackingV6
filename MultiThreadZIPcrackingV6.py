#!/usr/bin/env python3
"""
HPC Zip Cracker V6 - Devil's Edition
A high-performance Gatling-style brute force tool.
Optimized for 64GB RAM and multi-core i7/i9 architectures.
Tested and stable at 2000+ pwd/s on Acer Nitro hardware.
"""

import pyzipper
import argparse
import os
import multiprocessing
from tqdm import tqdm
from time import strftime

# --- CORE WORKER FUNCTION ---
def check_password(args):
    zip_path, password, opath = args
    try:
        # Standard high-performance decryption stream
        with pyzipper.AESZipFile(zip_path) as z_file:
            z_file.extractall(path=opath, pwd=password.encode('utf-8'))
            return password
    except Exception:
        return None

# --- MAIN EXECUTION BLOCK ---
def main():
    parser = argparse.ArgumentParser(description='HPC Zip Cracker V6 - Devil Edition')
    parser.add_argument('-z', required=True, help='Path to protected ZIP')
    parser.add_argument('-d', required=True, help='Path to wordlist')
    parser.add_argument('-o', help='Output directory', default=r'.\extracted_output')
    parser.add_argument('-c', type=int, help='Manual core count (Defaults to 50%%)')
    args = parser.parse_args()

    # Detects the total "barrels" available on your CPU
    total_cores = multiprocessing.cpu_count()
    use_cores = args.c if args.c else max(1, total_cores // 2)
    
    if not os.path.exists(args.z) or not os.path.exists(args.d):
        print(f"[!!] File Error: Check your filenames.")
        return

    # 1. Loading Phase (The 64GB RAM Optimization)
    print(f"[*] Loading wordlist into RAM... (Time: {strftime('%H:%M:%S')})")
    try:
        with open(args.d, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!!] Error: {e}")
        return

    print(f"[*] {len(passwords):,} passwords loaded. Using {use_cores} cores.")
    
    # 2. Attack Preparation
    tasks = [(args.z, p, args.o) for p in passwords]
    found_password = None

    # 3. Multiprocessing Pool (The Gatling Mechanism)
    print(f"[*] Releasing Hell... Progress bar should appear momentarily.")
    
    with multiprocessing.Pool(processes=use_cores) as pool:
        # Menacing Red bar for the Reddit Money Shot
        pbar = tqdm(total=len(tasks), unit="pwd", desc="Cracking", colour="red")
        
        # chunksize=1000 ensures continuous feeding of the core "barrels"
        for result in pool.imap_unordered(check_password, tasks, chunksize=1000):
            pbar.update(1)
            if result:
                found_password = result
                pool.terminate() 
                pbar.close()
                break
    
    # Hacker Green for the final "hit"
    GREEN_TEXT = "\033[92m"
    RESET_COLOR = "\033[0m"

    if found_password:
        print(f"\n\n{GREEN_TEXT}{'='*60}")
        print(f"[+] SUCCESS! PASSWORD: {found_password}")
        print(f"{'='*60}{RESET_COLOR}")
    else:
        print("\n[*] Attack complete. No match found.")

if __name__ == '__main__':
    # Prevents Windows child-process recursion
    multiprocessing.freeze_support()
    main()