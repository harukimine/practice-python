import re


def validate_price(value: str):
    print(re.match(r"\d+(,\d+)*$", value))


validate_price("1,234,567")
validate_price("1,234,567.89")
validate_price("234")
