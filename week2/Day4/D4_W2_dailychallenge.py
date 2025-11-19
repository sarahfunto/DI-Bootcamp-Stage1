
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"Le mot '{word}' n'a pas été trouvé."
        return count

    def most_common_word(self):
        words = self.text.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        if not freq:
            return None
        most_common = max(freq, key=freq.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)
    
    
text_from_file = Text.from_file("text.txt")
print("Fréquence du mot 'python' :", text_from_file.word_frequency("python"))