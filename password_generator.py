import random
import string

def generate(length=16, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return " ".join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Password length (default 16): ") or 16)
    print("Generated:", generate(length))