from db import DailyCardDatabase
from scryfall_api import fetch_random_white_card

db = DailyCardDatabase()


def update_card_of_the_day():
    new_card = fetch_random_white_card()
    if new_card:
        db.store_card(new_card["card_id"], new_card["name"], new_card["image_url"])
        print(f"New card of the day: {new_card['name']}")


if __name__ == "__main__":
    update_card_of_the_day()

