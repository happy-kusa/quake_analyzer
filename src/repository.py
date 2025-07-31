from src.database import get_connection
from src.models import AgriProduct

def save_products(products: list[AgriProduct]):
    conn = get_connection()
    cursor = conn.cursor()
    for p in products:
        cursor.execute("""
            INSERT OR IGNORE INTO agri_products (
                TransDate, TcType, CropCode, CropName,
                MarketCode, MarketName,
                Upper_Price, Middle_Price, Lower_Price,
                Avg_Price, Trans_Quantity
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p.TransDate, p.TcType, p.CropCode, p.CropName,
            p.MarketCode, p.MarketName,
            p.Upper_Price, p.Middle_Price, p.Lower_Price,
            p.Avg_Price, p.Trans_Quantity
        ))
    conn.commit()
    conn.close()

def fetch_recent(days: int = 7):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT TransDate, CropName, MarketName, Avg_Price, Trans_Quantity
        FROM agri_products
        ORDER BY TransDate DESC
        LIMIT ?
    """, (days,))
    rows = cursor.fetchall()
    conn.close()
    return rows
