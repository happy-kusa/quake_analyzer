import requests
import datetime
from src.models import AgriProduct

BASE_URL = "https://data.moa.gov.tw/api/v1/AgriProductsTransType/"
DEFAULT_CROP_CODE = "FJ3"
DEFAULT_MARKET_NAME = "台北一"

def build_today_url():
    now = datetime.datetime.now()
    roc_year = now.year - 1911
    date_str = f"{roc_year}.{now.month:02d}.{now.day:02d}"
    return (
        f"{BASE_URL}"
        f"?Start_time={date_str}"
        f"&End_time={date_str}"
        f"&CropCode={DEFAULT_CROP_CODE}"
        f"&MarketName={DEFAULT_MARKET_NAME}"
    )

def fetch_today_data() -> list[AgriProduct]:
    url = build_today_url()
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return [AgriProduct(**row) for row in data.get("Data", [])]
