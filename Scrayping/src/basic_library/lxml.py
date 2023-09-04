import os
import lxml.html
from util import fetch, save


URL = "https://gihyo.jp/dp"
SAVE_DIR = "output"


def main():
    html = fetch(URL)
    books = scrape_title_by_lxml(html, URL)
    os.makedirs(SAVE_DIR, exist_ok=True)
    save(books, f"{SAVE_DIR}/books.csv")


def scrape_title_by_lxml(html: str, base_url: str) -> list[dict]:
    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)
    for a in html.cssselect("#listBook > li > a[itemprop='url']"):
        url = a.get("href")
        print(url)
        title = a.cssselect("p[itemprop='name']")[0].text_content()
        books.append({"url": url, "title": title})
    return books


if __name__ == "__main__":
    main()
