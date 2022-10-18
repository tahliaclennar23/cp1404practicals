"""
Tahlia Clennar
CP1404 Practical 05- Word Occurrences
Program to count the occurrences of words in a string.
Estimate:25 minutes
"""

user_text = input("Enter text: ")
print(f"Text: {user_text}")
word_to_count = {}

for word in user_text.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length = max(len(word) for word in list(word_to_count.keys()))
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
