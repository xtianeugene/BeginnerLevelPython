import json, os

FILE = "contacts.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save(c):
    json.dump(c, open(FILE, "w"), indent=2)

def main():
    contacts = load()
    while True:
        print("\n1. Add 2. Search 3. List 4. Quit")
        c = input("Choice: ")

        if c == "1":
            name = input("Name: ")
            contacts[name] = {"phone": input("Phone: "), "email": input("Email: ")}
            save(contacts)
        elif c == "2":
            name = input("Search name: ")
            print(contacts.get(name, "Not found"))
        elif c == "3":
            for n, d in contacts.items():
                print(f"{n}. {d}")
        elif c == "4":
            break

if __name__ == "__main__":
    main()