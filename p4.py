sentence = "the cat and the hat and the bat"

# 1. Split sentence into words
words = sentence.split()

# 2. Count each word using a dictionary
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

# 3. Print the dictionary
print(counts)

# 4. Find the most common word
most_common = max(counts, key=counts.get)
print(most_common, counts[most_common])
