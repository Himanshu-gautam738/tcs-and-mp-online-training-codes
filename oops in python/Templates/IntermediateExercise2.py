from numbers import Number

def upload(data: Number) -> None:
    if not isinstance(data, Number):
        raise TypeError(f"Invalid type: {type(data).__name__}. Only numeric types are allowed.")
    print(f"Uploading: {data}")

# Usage with numeric types
upload(42)        # Integer
upload(3.1415)    # Float (Double equivalent in Java)

# Trying with a string
try:
    upload("hello")  # This will raise TypeError
except TypeError as e:
    print(e)
