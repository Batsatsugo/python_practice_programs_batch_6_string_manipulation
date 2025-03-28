# DECLARE text, words, capitalized_word, capitalized_words

# text = input("Enter a string: ")
text = input("Enter a string: ")

# words = text.split()
words = text.split()

# capitalized_words = []
# FOR word in words:
#     capitalized_word = word[0].upper() + word[1:].lower() if word else ""
#     capitalized_words.append(capitalized_word)
capitalized_words = []
for word in words:
     capitalized_word = word[0].upper() + word[1:].lower() if word else ""
     capitalized_words.append(capitalized_word)

# result = " ".join(capitalized_words)
# PRINT("Formatted String:", result)
result = " ".join(capitalized_words)
print("Formatted String:", result)
