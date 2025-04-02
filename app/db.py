import sqlite3
from datetime import datetime

DB_PATH = "../data/cards.db"


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


def get_today_card():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = datetime.today().strftime("%Y-%m-%d")
    cursor.execute("SELECT * FROM daily_card WHERE date_shown = ?", (today,))
    result = cursor.fetchone()
    conn.close()
    return result


def store_card(card_id, name, image_url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = datetime.today().strftime("%Y-%m-%d")

    cursor.execute("DELETE FROM daily_card WHERE date_shown = ?", (today,))
    cursor.execute("INSERT INTO daily_card (card_id, name, date_shown, image_url) VALUES (?, ?, ?, ?)",
                   (card_id, name, today, image_url))

    conn.commit()
    conn.close()

