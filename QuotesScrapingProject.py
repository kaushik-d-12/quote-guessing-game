import requests
from bs4 import BeautifulSoup
from random import choice

BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():
    url = "/page/1"
    all_quotes = []

    while url:
        try:
            res = requests.get(f"{BASE_URL}{url}", timeout=10)
            res.raise_for_status()
        except requests.RequestException as e:
            print(f"Could not access the website: {e}")
            return []

        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(strip=True),
                "author": quote.find(class_="author").get_text(strip=True),
                "bio-data": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

    return all_quotes


def get_author_hint(quote):
    try:
        res = requests.get(f"{BASE_URL}{quote['bio-data']}", timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        birth_date = soup.find(class_="author-born-date").get_text(strip=True)
        birth_place = soup.find(class_="author-born-location").get_text(strip=True)

        return f"The author was born on {birth_date} {birth_place}."
    except requests.RequestException:
        return "Sorry, the author information could not be retrieved."
    except AttributeError:
        return "Sorry, the author information could not be found."


def play_game(quotes):
    print("\nWelcome to the Quote Guessing Game!")

    quote = choice(quotes)
    remaining_guesses = 4

    print("\nHere's a quote:")
    print(quote["text"])

    while remaining_guesses > 0:
        guess = input(
            f"\nWho said this quote? "
            f"Guesses remaining: {remaining_guesses}\n"
        ).strip()

        remaining_guesses -= 1

        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            return

        if remaining_guesses == 3:
            print(f"Here's a hint: {get_author_hint(quote)}")

        elif remaining_guesses == 2:
            print(
                f"Here's a hint: The author's first name "
                f"starts with: {quote['author'][0]}"
            )

        elif remaining_guesses == 1:
            name_parts = quote["author"].split()

            if len(name_parts) >= 2:
                last_initial = name_parts[-1][0]
                print(
                    f"Here's a hint: The author's last name "
                    f"starts with: {last_initial}"
                )
            else:
                print("Here's a hint: The author's name has only one part.")

        else:
            print(f"Sorry! You ran out of guesses.")
            print(f"The answer was {quote['author']}")
            return


def main():
    quotes = scrape_quotes()

    if not quotes:
        print("No quotes could be retrieved. Exiting the game.")
        return

    while True:
        play_game(quotes)

        while True:
            again = input("\nPlay again (y/n)? ").strip().lower()

            if again in ("y", "yes"):
                break
            elif again in ("n", "no"):
                print("Exiting game. Goodbye!")
                return
            else:
                print("Please enter y/yes or n/no.")


if __name__ == "__main__":
    main()