import re
import os
import requests
import lxml.html
import csv


URL = "https://gihyo.jp/dp"
SAVE_DIR = "output"


def main():
    html = fetch(URL)
    books = scrape_title_by_lxml(html, URL)
    os.makedirs(SAVE_DIR, exist_ok=True)
    save(books, f"{SAVE_DIR}/books.csv")


def fetch(url: str) -> str:
    r = requests.get(url)
    r.encoding = estimate_encoding(r)
    return r.text


def estimate_encoding(r: requests.Response):
    scanned_text = r.content[:1024].decode("ascii", errors="replace")
    charset = re.search(r"charset=['\"]?([\w-]+)", scanned_text)
    if charset:
        return charset.group(1)
    else:
        return r.apparent_encoding


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


def save(books: list[dict], file_path: str):
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, ["url", "title"])
        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    main()
