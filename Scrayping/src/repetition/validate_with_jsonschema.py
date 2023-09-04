from jsonschema import validate

# object is a dictionary

schema = {
    "type": "object",
    "properties": {
        "price": {"type": "string", "pattern": r"\d+(,\d+)*$"},
        "name": {"type": "string"},
    },
}

examples = [
    {"name": "foo", "price": "1,234,567"},
    {"name": "bar", "price": "free"},
    {"name": "baz", "price": "78.90"},
]

for example in examples:
    print(example, end=" -> ")
    try:
        validate(example, schema)
        print("OK")
    except Exception as e:
        print(f"NG: {e}")
