# DECLARE word, suffix

# word = input("Enter a word: ")
# suffix = input("Enter the suffix to check if it matches the end part: ")
word = input("Enter a word: ")
suffix = input("Enter the suffix to check if it matches the end part: ")

# IF word [-len(suffix):] == suffix:
#     print("True")
# ELSE:(
#     print("False"))
if word[-len(suffix):] == suffix:
    print("True")
else:
    print("False")