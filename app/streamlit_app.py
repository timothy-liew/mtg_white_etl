import streamlit as st
import sqlite3
from db import get_today_card

DB_PATH = "../data/cards.db"

def fetch_past_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, date_shown, image_url FROM daily_card ORDER BY date_shown LIMIT 7")
    past_cards = cursor.fetchall()
    conn.close()
    return past_cards


st.title("Tim's Monowhite Card of the Day")

card = get_today_card()
if card:
    st.subheader(f"Today's Card: {card[1]}")
    st.image(card[3], width=400)
else:
    st.warning("No card has been selected for the day.")

if st.button("View Past Cards"):
    past_cards = fetch_past_cards()
    if past_cards:
        st.subheader("Past Cards")
        for name, date, img in past_cards:
            st.write(f"**{name}** ({date})")
            st.image(img, width=200)
    else:
        st.info("No past cards recorded")