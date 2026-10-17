CONVERSIONS = {
    "km_to_miles": lambda x: x * 0.621371,
    "miles_to_km": lambda x: x / 0.621371,
    "kg_to_lbs": lambda x: x * 2.20462,
    "lbs_to_kg": lambda x: x / 2.20462,
    "c_to_f": lambda x: (x * 9/5) + 32,
    "f_to_c": lambda x: (x - 32) * 5/9,
}

def main():
    print("Available:", ", ".join(CONVERSIONS))
    choice = input("Conversion: ").strip()
    if choice in CONVERSIONS:
        value = float(input("Value: "))
        print(f"Result: {CONVERSIONS[choice](value):.4f}")
    else:
        print("Unknown conversion.")

if __name__ == "__main__":
    main()