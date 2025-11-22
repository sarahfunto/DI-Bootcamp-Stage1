from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()

    while True:
        print("\n ANAGRAM MENU ")
        print("1. Enter a word")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            user_word = input("Enter a word: ").strip()

            # VALIDATION
            if " " in user_word:
                print("Error: Only one word allowed.")
                continue

            if not user_word.isalpha():
                print("Error: Only alphabetic characters allowed.")
                continue

            # VALID WORD?
            if not checker.is_valid_word(user_word):
                print(f'YOUR WORD: "{user_word.upper()}"')
                print("This is NOT a valid English word.")
                continue

            # FIND ANAGRAMS
            anagrams = checker.get_anagrams(user_word)

            print(f'\nYOUR WORD: "{user_word.upper()}"')
            print("✔ This is a valid English word.")

            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print("No anagrams found.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()
