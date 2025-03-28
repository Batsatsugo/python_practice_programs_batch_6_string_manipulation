# DECLARE word, new_word, space

# word = "  Jian Cora"
word = input("Enter a word with spaces in front before the word: ")

# space = 0

space = 0
# WHILE space < len(word) and word[space] == " ":
#     space += 1

while space < len(word) and word[space] == " ":
    space += 1

# new_word = word[space:]
new_word =  word[space:]

# PRINT("Original word:", repr(word))
# PRINT("Modified word:", repr(new_word))
print("Original word:", repr(word))
print("Modified word:", repr(new_word))