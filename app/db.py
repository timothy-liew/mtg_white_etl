import sqlite3
from datetime import datetime

DB_PATH = "data/cards.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_card (
            card_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            date_shown TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()