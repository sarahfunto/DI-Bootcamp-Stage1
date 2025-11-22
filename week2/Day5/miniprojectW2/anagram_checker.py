import os
class AnagramChecker:
    def __init__(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sowpods.txt")

        with open(file_path, "r") as file:
            self.word_list = {word.strip().lower() for word in file}

    def is_valid_word(self, word):
        """Check if the given word exists in the dictionary."""
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """Check if two words are anagrams."""
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        """Return all anagrams of the given word."""
        word = word.lower()
        anagrams = []

        for candidate in self.word_list:
            if candidate != word and self.is_anagram(word, candidate):
                anagrams.append(candidate)

        return anagrams
