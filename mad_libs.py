def main():
    words = {}
    for prompt in ["a name", "an adjective", "a noun", "a verb", "a place"]:
        words[prompt] = input(f"Enter {prompt}: ")
    story = (
        f" One day, {words['a name']}  went to {words['a place']} with a very "
        f"{words['an adjective']} {words['a noun']}. They decided to "
        f"{words['a verb']} all day long."
    )
    print("\n" + story)

if __name__ == "__main__":
    main()