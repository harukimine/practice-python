from xml.etree import ElementTree
import os
from util import fetch, save


URL = "https://gihyo.jp/feed/rss2"
SAVE_DIR = "output"


def main():
    rss = fetch(URL)
    books = scrape(rss)
    os.makedirs(SAVE_DIR, exist_ok=True)
    save(books, f"{SAVE_DIR}/rss_books.csv")


def scrape(rss: str) -> list[dict]:
    books = []
    root = ElementTree.fromstring(rss)
    for item in root.findall("channel/item"):
        url = item.find("link").text
        title = item.find("title").text
        books.append({"url": url, "title": title})
    return books


if __name__ == "__main__":
    main()
