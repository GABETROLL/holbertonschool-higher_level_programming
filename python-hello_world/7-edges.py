#!/usr/bin/python3
word = "Holberton"        # strings with the letters from word's:
word_first_3 = word[:3]   # first 3 letters
word_last_2 = word[-2:]   # last 2 letters ('first' meaning "at index 0")
middle_word = word[1:-1]  # second letter to second-to-last letters
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
