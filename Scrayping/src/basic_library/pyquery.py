from pyquery import PyQuery as pq
import os
from util import fetch, save


URL = "https://gihyo.jp/dp"
SAVE_DIR = "output"


def main():
    html = fetch(URL)
    books = scrape_title(html)
    os.makedirs(SAVE_DIR, exist_ok=True)
    save(books, f"{SAVE_DIR}/books.csv")


def scrape_title(html: str, base_url: str = URL) -> list[dict]:
    """
    引数で指定したHTMLから書籍のタイトルを抜き出す
    """
    books = []
    root = pq(html)
    root.make_links_absolute(base_url)
    for a in root("#listBook > li > a[itemprop='url']"):
        url = root(a).attr("href")
        title = root(a).find("p[itemprop='name']").eq(0).text()
        books.append({"url": url, "title": title})
    return books
