import requests
import time

SCRYFALL_RANDOM_URL = "https://api.scryfall.com/cards/random?q=c%3Aw"


def fetch_random_white_card():
    while True:
        response = requests.get(SCRYFALL_RANDOM_URL)
        if response.status_code == 200:
            data = response.json()
            if data.get("colors") == ["W"]:
                return {
                    "card_id": data["id"],
                    "name": data["name"],
                    "image_url": data["image_uris"]["normal"] if "image_uris" in data else None
                }
        time.sleep(1)


if __name__ == "__main__":
    card = fetch_random_white_card()
    print(card)

