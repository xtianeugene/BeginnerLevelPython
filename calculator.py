def calculate(a, op, b):
    ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b else None}
    return ops.get(op)

def main():
    while True:
        try:
            a = float(input("First number: "))
            op = input("Operator (+ - * /): ").strip()
            b = float(input("Second number: "))
            result = calculate(a, op, b)
            if result is None:
                print("Invalid operation or division by zero.")
            else:
                print(f"Result: {result}")
        except ValueError:
            print("Invalid input.")
        if input("Again? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()