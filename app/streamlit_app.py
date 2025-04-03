import streamlit as st
from db import DailyCardDatabase
from daily_fetch import update_card_of_the_day

db = DailyCardDatabase()


st.title("Tim's Monowhite Card of the Day")

# if st.button("Refresh Card"):
#     update_card_of_the_day() # Updates database card
#     st.rerun()

today_card = db.get_today_card()

if today_card:
    st.subheader(f"Today's Card: {today_card[1]}")
    st.image(today_card[3], width=400)
else:
    st.warning("No card has been selected for the day.")

if st.button("View Past Cards"):
    past_cards = db.fetch_past_cards()
    if past_cards:
        st.subheader("Past Cards")
        columns = st.columns(len(past_cards))

        for i, (name, date_shown, image_url) in enumerate(past_cards):
            with columns[i]:  # Place each card in a separate column
                st.image(image_url, caption=f"{name}, ({date_shown})", use_container_width=True)
    else:
        st.info("No past cards recorded")