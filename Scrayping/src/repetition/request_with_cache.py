import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache


URL = "https://gihyo.jp/dp"

session = requests.Session()
cached_session = CacheControl(session, cache=FileCache(".webcache"))
response = cached_session.get(URL)
print(f"{response.from_cache=}")
