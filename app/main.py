from db import init_db, get_today_card, store_card
from scryfall_api import fetch_random_white_card


def update_card_of_the_day():
    init_db()

    new_card = fetch_random_white_card()
    if new_card:
        store_card(new_card["card_id"], new_card["name"], new_card["image_url"])
        print(f"New card of the day: {new_card['name']}")

if __name__ == "__main__":
    update_card_of_the_day()