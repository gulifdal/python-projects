# Project 4 - Word Counter
# Author: Gul Ifdal

sentence = input("Enter a sentence: ")

# Split the sentence into a list of lowercase words
words = sentence.lower().split()

# TODO: count total words (hint: len())
total_words = len(words)

# TODO: count total characters without spaces (hint: remove spaces first)
total_chars = len(sentence.replace(" ", ""))

# TODO: build a word frequency dictionary

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# TODO: print all results

print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print("Word frequency:")
for word in frequency:
    print(f"{word} -> {frequency[word]}")

# --- Bonus Challenge ---
# Strip punctuation from the sentence before processing

punctuation = ".,!?;:"
for char in punctuation:
    sentence = sentence.replace(char, "")
