"""
Tahlia Clennar
CP1404 Practical 05- Word Occurrences
Program to count the occurrences of words in a string.
"""

user_text = input("Enter text: ")
print(f"Text: {user_text}")
word_to_count = {}

for word in user_text.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(word_to_count):
    print(f"{word} : {word_to_count[word]}")
