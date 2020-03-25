import requests


def demo() -> int:
    return requests.get("https://tw.amazingtalker.com/tutors/japanese").status_code
