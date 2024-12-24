5.def is_palindrome_slicing(s):
    # Convert the string to lowercase and check if it equals its reverse
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    return s == s[::-1]

# Example usage
print(is_palindrome_slicing("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_slicing("hello"))  # Output: False