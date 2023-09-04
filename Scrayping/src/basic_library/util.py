import re
import requests
import csv


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


def save(books: list[dict], file_path: str):
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, ["url", "title"])
        writer.writeheader()
        writer.writerows(books)
