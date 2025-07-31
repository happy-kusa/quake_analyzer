import time
import datetime
import sys
from src.config import *
from src.fetcher import fetch_today_data
from src.repository import save_products

def wait_until_next_interval(interval_minutes: int):
    now = datetime.datetime.now()
    delta_minutes = interval_minutes - (now.minute % interval_minutes)
    next_time = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=delta_minutes)
    seconds_until_next = (next_time - now).total_seconds()
    print(f"[{now}] 等待 {int(seconds_until_next)} 秒直到下一次觸發...")
    time.sleep(seconds_until_next)

def run_periodic_task():
    now = datetime.datetime.now()
    print(f"[{now}] 開始抓取資料...")
    products = fetch_today_data()
    save_products(products)
    print(f"[{now}] 已寫入 {len(products)} 筆資料")

def run_forever():
    print(f"常駐程式啟動，每 {INTERVAL_MINUTES} 分鐘觸發一次任務...")
    while True:
        wait_until_next_interval(INTERVAL_MINUTES)
        run_periodic_task()
