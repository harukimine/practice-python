import re
import time
import requests
import lxml.html
from pymongo import MongoClient
from typing import Generator


URL = "https://gihyo.jp/dp"


def main():
    client = MongoClient("localhost", 27017)
    collection = client.scraping.ebooks
    collection.create_index("key", unique=True)

    session = requests.Session()
    response = requests.get(URL)
    urls = scrape_list_page(response)
    for url in urls:
        key = extract_key(url)
        ebook = collection.find_one({"key": key})
        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
            collection.insert_one(ebook)
        print(ebook)


def scrape_list_page(response: requests.Response) -> Generator[str, None, None]:
    html = lxml.html.fromstring(response.content)
    html.make_links_absolute(response.url)
    for a in html.cssselect("#listBook > li > a[itemprop='url']"):
        url = a.get("href")
        yield url


def extract_key(url) -> str:
    m = re.search(r"/([^/]+)$", url)
    return m.group(1)


def scrape_detail_page(response: requests.Response) -> dict[str, any]:
    html = lxml.html.fromstring(response.content)
    ebook = {
        "url": response.url,
        "key": extract_key(response.url),
        "title": html.cssselect("#bookTitle")[0].text_content(),
        "price": html.cssselect(".buy")[0].text.strip(),
        "content": [
            normalize_spaces(h3.text_content())
            for h3 in html.cssselect("#content > h3")
        ],
    }
    return ebook


def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


if __name__ == "__main__":
    main()
