import argparse
from src.repository import fetch_recent

def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show", action="store_true", help="顯示最近 7 天資料並退出")
    parser.add_argument("--days", type=int, default=7, help="指定顯示天數")
    args = parser.parse_args()

    if args.show:
        rows = fetch_recent(args.days)
        print(f"最近 {args.days} 天資料：")
        for r in rows:
            print(f"日期 {r[0]} | {r[1]} @ {r[2]} | 平均價 {r[3]} | 交易量 {r[4]}")
        return True
    return False
