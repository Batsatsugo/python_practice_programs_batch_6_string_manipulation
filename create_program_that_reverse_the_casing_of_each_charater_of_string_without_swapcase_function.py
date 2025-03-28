# DECLARE word, new_word,

# word = input("Enter a word: ")
word = input("Enter a word: ")

# new_word = ""
# for char in word:
# if 'a' <= char <= 'z':
#     new_word += chr(ord(char) - 32)
# elif 'A' <= char <= 'Z':
#     new_word += chr(ord(char) + 32)
# else:
#     new_word += char
new_word = ""
for char in word:
    if 'a' <= char <= 'z':
        new_word += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        new_word += chr(ord(char) + 32)
    else:
        new_word += char

# print("Swapped case word:", new_word)
print("Swapped case word:", new_word)
