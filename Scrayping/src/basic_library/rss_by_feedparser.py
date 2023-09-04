import feedparser
from util import save


URL = "https://b.hatena.ne.jp/hotentry/it.rss"
SAVE_DIR = "output"


def main():
    rss = fetch(URL)
    books = scrape(rss)
    save(books, f"{SAVE_DIR}/rss_books.csv")


def fetch(url: str) -> str:
    return feedparser.parse(url)


def scrape(rss: str) -> list[dict]:
    books = []
    for entry in rss.entries:
        url = entry.link
        title = entry.title
        books.append({"url": url, "title": title})
    return books


if __name__ == "__main__":
    main()
