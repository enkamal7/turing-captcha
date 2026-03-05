import os
import time
import sys

RESET     = "\033[0m"
BOLD      = "\033[1m"
DIM       = "\033[2m"
RED       = "\033[91m"
GREEN     = "\033[92m"
YELLOW    = "\033[93m"
BLUE      = "\033[94m"
CYAN      = "\033[96m"
WHITE     = "\033[97m"
GRAY      = "\033[90m"
BLACK     = "\033[30m"
MAGENTA   = "\033[95m"
BG_GREEN  = "\033[42m"
BG_RED    = "\033[41m"
BG_YELLOW = "\033[43m"

WIDTH = 64

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewrite(text, delay=0.018, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner(title, subtitle="", color=CYAN):
    print()
    print(color + "+" + "=" * WIDTH + "+" + RESET)
    print(color + "|" + RESET + "  " + BOLD + f"{title:<{WIDTH - 2}}" + RESET + color + "|" + RESET)
    if subtitle:
        print(color + "|" + RESET + "  " + GRAY + f"{subtitle:<{WIDTH - 2}}" + RESET + color + "|" + RESET)
    print(color + "+" + "=" * WIDTH + "+" + RESET)

def box(lines, color=GRAY):
    print(color + "+" + "-" * WIDTH + "+" + RESET)
    for line in lines:
        print(color + "| " + RESET + f"{line:<{WIDTH - 1}}" + color + "|" + RESET)
    print(color + "+" + "-" * WIDTH + "+" + RESET)

def status(label, value, lc=CYAN, vc=WHITE):
    print(f"  {lc}{label:<22}{RESET} {vc}{value}{RESET}")

def divider(char="-", color=GRAY):
    print(color + char * WIDTH + RESET)

def prompt(msg, color=YELLOW):
    return input(f"\n  {color}>{RESET} {msg}: ").strip()

def pause(msg="Press ENTER to continue..."):
    input(f"\n  {GRAY}{msg}{RESET}")

def result_pass(msg):
    print(f"\n  {BOLD}{BG_GREEN}{BLACK}  PASS  {RESET}  {GREEN}{msg}{RESET}")

def result_fail(msg):
    print(f"\n  {BOLD}{BG_RED}{WHITE}  FAIL  {RESET}  {RED}{msg}{RESET}")

def result_warn(msg):
    print(f"\n  {BOLD}{BG_YELLOW}{BLACK}  WARN  {RESET}  {YELLOW}{msg}{RESET}")

def thinking(label="Processing", duration=1.5):
    frames = ["   ", ".  ", ".. ", "..."]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {GRAY}{label}{frames[i % 4]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def menu(title, options, color=CYAN):
    print(f"\n  {BOLD}{color}{title}{RESET}")
    divider(color=GRAY)
    for key, label in options:
        print(f"  {YELLOW}[{key}]{RESET}  {label}")
    divider(color=GRAY)
    return prompt("Select", color=YELLOW)
