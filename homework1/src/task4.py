# Task 4: calculate a discounted price using a percentage rate
def calculate_discount(price, discount):
    return price * (1 - discount / 100)


if __name__ == "__main__":
    print(calculate_discount(100, 10))
