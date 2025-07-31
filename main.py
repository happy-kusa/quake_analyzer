#!/usr/bin/env python3

import time
import datetime
import requests

INTERVAL_MINUTES = 1

def task():

    url = (
        "https://data.moa.gov.tw/api/v1/AgriProductsTransType/"
        "?Start_time=114.07.01"
        "&End_time=114.07.10"
        "&CropCode=FJ3"
        "&CropName"
        "&MarketName=台北一"
    )

    headers = {
        'accept': 'application/json',
        'Cookie': 'ASP.NET_SessionId=ennenv3x13k01ulh45dskged'
    }
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def do_periodic_task():
    now = datetime.datetime.now()
    print(f"[{now}] {task()}")



def wait_until_next_interval(interval_minutes):
    now = datetime.datetime.now()
    delta_minutes = interval_minutes - (now.minute % interval_minutes)
    next_time = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=delta_minutes)
    seconds_until_next = (next_time - now).total_seconds()
    print(f"[{now}] 等待 {int(seconds_until_next)} 秒直到下一次觸發...")
    time.sleep(seconds_until_next)


def main():
    print(f"常駐程式啟動，每 {INTERVAL_MINUTES} 分鐘觸發一次任務...")
    while True:
        wait_until_next_interval(INTERVAL_MINUTES)
        do_periodic_task()


if __name__ == "__main__":
    main()





