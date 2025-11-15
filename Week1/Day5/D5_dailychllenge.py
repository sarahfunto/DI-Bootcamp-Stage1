#challenge 1 :

input_string = input("Enter words: ")
word_list = input_string.split()
word_list.sort()
sorted_string = ','.join(word_list)
print(sorted_string)

#challenge 2 :
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    max_length = 0
    for word in words:
        
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    return longest
# Test the function
print(longest_word("Margaret's toy is a pretty doll."))      # Margaret's
print(longest_word("A thing of beauty is a joy forever."))   # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness
