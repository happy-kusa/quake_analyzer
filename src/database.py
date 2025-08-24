import sqlite3

DB_FILE = "agri_data.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS agri_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                TransDate TEXT,
                TcType TEXT,
                CropCode TEXT,
                CropName TEXT,
                MarketCode TEXT,
                MarketName TEXT,
                Upper_Price REAL,
                Middle_Price REAL,
                Lower_Price REAL,
                Avg_Price REAL,
                Trans_Quantity REAL,
                UNIQUE(TransDate, CropCode, MarketCode)
            )
        """
    )
    conn.commit()
    conn.close()
