from colorama import Fore

"""
-   src/log.py
-   Author: @kexecq
-   Date: 30/09/2024
"""

def log_err(msg: str):
    print(f"[pinpy]: {Fore.RED}{msg}{Fore.RESET}")

def log_out(msg: str):
    print(f"[pinpy]: {Fore.GREEN}{msg}{Fore.RESET}")
