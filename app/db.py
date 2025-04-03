import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "cards.db")

class DailyCardDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.init_db()

    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_card (
                card_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                date_shown TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
        """)
        self.conn.commit()

    @staticmethod
    def get_today_card():
        today = datetime.today().strftime("%Y-%m-%d")
        with sqlite3.connect(DB_PATH) as conn:  # New short-lived connection
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM daily_card WHERE date_shown = ?", (today,))
            return cursor.fetchone()

    def store_card(self, card_id, name, image_url):
        today = datetime.today().strftime("%Y-%m-%d")
        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM daily_card WHERE date_shown = ?", (today,))
        cursor.execute(
            "INSERT INTO daily_card (card_id, name, date_shown, image_url) VALUES (?, ?, ?, ?)",
            (card_id, name, today, image_url)
        )
        self.conn.commit()

    @staticmethod
    def fetch_past_cards():
        with sqlite3.connect(DB_PATH) as conn:  # New short-lived connection
            cursor = conn.cursor()
            cursor.execute("SELECT name, date_shown, image_url FROM daily_card ORDER BY date_shown DESC LIMIT 7")
            return cursor.fetchall()

    def close(self):
        self.conn.close()
