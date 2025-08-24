#!/usr/bin/env python3.12

import sys
import signal
import argparse
from src.database import init_db
from src.scheduler import run_forever
from src.repository import fetch_recent

VERSION = "0.0.1"

def cli_handle():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show", action="store_true", help="顯示最近 N 天資料並退出")
    parser.add_argument("--days", type=int, default=7, help="指定顯示天數")
    parser.add_argument("--version", action="store_true", help="顯示版本")
    args = parser.parse_args()

    match args:
        case _ if args.show:
            rows = fetch_recent(args.days)
            print(f"最近 {args.days} 天資料：")
            for r in rows:
                print(f"日期 {r[0]} | {r[1]} @ {r[2]} | 平均價 {r[3]} | 交易量 {r[4]}")
            return True

        case _ if args.version:
            print(f"v{VERSION}")
            return True

        case _:
            return False

def sigint_handle(sig, frame):
    print("\n收到 Ctrl+C，程式準備結束...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, sigint_handle)
    init_db()
    if not cli_handle():
        run_forever()

if __name__ == "__main__":
    main()

