# 1. Squares of even numbers from 1 to 10
squares = [n**2 for n in range(1, 11) if n % 2 == 0]
print(squares)

# 2. Dictionary mapping each word to its length
words = ["ai", "python", "data"]
lengths = {word: len(word) for word in words}
print(lengths)

# 3. Unique letters of "banana", sorted
letters = sorted(set("banana"))
print(letters)