import requests
from tenacity import retry, stop_after_attempt, wait_exponential


TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)
RETRY_MAX = 3
URL = "http://httpbin.org/status/200,404,503"


def main():
    response = fetch(URL)
    if 200 <= response.status_code < 300:
        print("Success!")
    else:
        print("Error!")


@retry(stop=stop_after_attempt(RETRY_MAX), wait=wait_exponential(multiple=1))
def fetch(url: str) -> requests.Response:
    print(f"Retrying... (url: {url})")
    response = requests.get(url)
    if response.status_code not in TEMPORARY_ERROR_CODES:
        return response
    raise Exception(f"Temporary Error: {response.status_code}")
