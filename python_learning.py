def greet(name: str) -> str:
    return f"Hello, {name}!"


def add_numbers(first: int, second: int) -> int:
    return first + second


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("Python learner"))
    print(add_numbers(2, 3))
    print(is_even(4))
