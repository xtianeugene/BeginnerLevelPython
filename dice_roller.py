import random
from collections import Counter

def roll(sides=6, count=1):
    return [random.randint(1, sides) for _ in range(count)]

def main():
    sides = int(input("Sides per die (default 6): ") or 6)
    count = int(input("Number of dice: ") or 1)
    results = roll(sides, count)
    print("Rolls: ", results, "| Total:", sum(results))
    print("Frequency:", dict(Counter(results)))

if __name__ == "__main__":
    main()