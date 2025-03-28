# DECLARE word, result,

# word = input("Enter a word: ")
# result = ""
word = input("Enter a word: ")
result = ""

# FOR char in word:
#     IF "A"<= char <= "Z":
#         result += chr(ord(char) + 32)
#     ELSE:
#         result += char
for char in word:
    if "A" <= char <= "Z":
        result += chr(ord(char) + 32)
    else:
        result += char

# PRINT("Lowercase word: ", result)
print("Lowercase word: ", result)