import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from util import fetch, save


URL = "https://gihyo.jp/dp"
SAVE_DIR = "output"


def main():
    html = fetch(URL)
    books = scrape_title_by_bs4(html, URL)
    os.makedirs(SAVE_DIR, exist_ok=True)
    save(books, f"{SAVE_DIR}/books.csv")


def scrape_title_by_bs4(html: str, base_url: str) -> list[dict]:
    books = []
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.select("#listBook > li > a[itemprop='url']"):
        url = urljoin(base_url, a.get("href"))
        title = a.select("p[itemprop='name']")[0].text
        books.append({"url": url, "title": title})
    return books
