# Quote Guessing Game

A Python command-line game that scrapes quotes and author information from [Quotes to Scrape](https://quotes.toscrape.com/) and challenges the user to identify the author.

## Features

* Scrapes quotes and author information from a website
* Uses Requests and BeautifulSoup for web scraping and HTML parsing
* Randomly selects a quote for each round
* Provides progressively informative hints
* Allows the user to play multiple rounds
* Handles common network and input errors

## Technologies Used

* Python
* Requests
* BeautifulSoup
* HTML parsing

## How It Works

1. The program scrapes quotes from multiple pages of the website.
2. The scraped quotes and author information are stored in Python data structures.
3. A quote is randomly selected.
4. The user gets four attempts to identify the author.
5. Hints are progressively provided after incorrect guesses.
6. The user can choose to play another round.

## How to Run

Install the required packages:

```bash
pip install requests beautifulsoup4
```

Then run:

```bash
python QuotesScrapingProject.py
```
