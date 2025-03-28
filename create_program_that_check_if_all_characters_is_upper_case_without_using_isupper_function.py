# DECLARE word, all_upper

# word = input("Enter a word: ")
word = input("Enter a word: ")

# all_upper = True
# FOR char in word:
#     IF 'a' <= char <= 'z':
#         all_upper = False
#         BREAK
all_upper = True
for char in word:
    if "a" <= char <= "z":
        all_upper = False
        break

# IF all_upper:
#     print("The word is in uppercase.")
# ELSE:
#     print("The word is not in uppercase.")
if all_upper:
    print("The word is in uppercase.")
else:
    print("The word is not in uppercase.")