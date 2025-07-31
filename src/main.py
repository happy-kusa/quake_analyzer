#!/usr/bin/env python3.12

import sys
import signal
from src.cli import run_cli
from src.database import init_db
from src.scheduler import run_forever

def handle_sigint(sig, frame):
    print("\n收到 Ctrl+C，程式準備結束...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handle_sigint)
    init_db()
    if not run_cli():
        run_forever()

if __name__ == "__main__":
    main()

