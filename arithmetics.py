from cs50 import get_int

def main():
    x = get_int("x: ")
    y = get_int("y: ")
    print(f"{x} plus {y} is {x + y}")
    print(f"{x} minus {y} is {x - y}")
    print(f"{x} times {y} is {x * y}")
    print(f"{x} truly divided by {y} is {x/y}")
    print(f"{x} floor divided by {y} is {x//y}")
    print(f"remainder of {x} divided by {y} is {x%y}")

if __name__ == "__main__":
    main()


