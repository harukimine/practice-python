import requests
import time


TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)
RETRY_MAX = 3
URL = "http://httpbin.org/status/200,404,503"


def main():
    response = fetch(URL)
    if 200 <= response.status_code < 300:
        print("Success!")
    else:
        print("Error!")


def fetch(url: str, max_retries: int = RETRY_MAX) -> requests.Response:
    for num_retries in range(1, max_retries + 1):
        try:
            response = requests.get(url)
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response
            print(f"Temporary Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Exception: {e}")
        print(f"Retrying... (num_retries: {num_retries})")
        time.sleep(2**num_retries)
    raise Exception("Too many retries")


if __name__ == "__main__":
    main()
