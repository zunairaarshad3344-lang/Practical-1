word = "Programming"

# 1. Reverse the word
print(word[::-1])

# 2. First 3 and last 3 characters
print(word[:3], word[-3:])

# 3. Count the letter "m"
print(word.count("m"))

# 4. Check palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"), is_palindrome("python"))