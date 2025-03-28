# DECLARE word,new_word, prefix

# word = input("Enter a word: ")
word = input("Enter a word: ").strip()

# prefix = input(:Enter the prefix to be removed:")
prefix = input("Enter the prefix to remove: ").strip()

# IF word[:len(prefix)] == prefix:
#     new_word = word[len(prefix):]
# ELSE:
#     new_word = word
if len(prefix) <= len(word) and word[:len(prefix)] == prefix:
    new_word = word[len(prefix):]
else:
    new_word = word

# PRINT("Original word:", repr(word))
# PRINT("Modified word:", repr(new_word))
print("Original word:", repr(word))
print("Modified word:", repr(new_word))