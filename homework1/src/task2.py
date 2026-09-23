# Task 2: create a dictionary showing common Python data types
def datatypes():
    data = {
        "string": str("Hello World"),
        "integer": int(100),
        "float": float(0.5),
        "boolean": bool(True),
    }
    for key, value in data.items():
        print(f"{key}: {value}")
    return data


if __name__ == "__main__":
    datatypes()