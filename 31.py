  

SOLUTION :


1.def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial_for_loop(5))  # Output: 120



2.def is_prime_for_loop(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime_for_loop(11))  # Output: True
print(is_prime_for_loop(15))  # Output: False



3.def fibonacci_for_loop(terms):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(terms):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print(fibonacci_for_loop(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



4.def reverse_string_slicing(s):
    return s[::-1]

# Example usage
print(reverse_string_slicing("hello"))  # Output: "olleh"


5.def is_palindrome_slicing(s):
    # Convert the string to lowercase and check if it equals its reverse
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    return s == s[::-1]

# Example usage
print(is_palindrome_slicing("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_slicing("hello"))  # Output: False


6.def pattern_for_loop(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Example usage
pattern_for_loop(4)


7.def triangle_for_loop(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join(str(x) for x in range(1, 2 * i)))
        
# Example usage
triangle_for_loop(3)


8.def alphabet_pattern_for_loop(n):
    for i in range(1, n + 1):
        # Calculate spaces for the current row
        spaces = ' ' * (n - i) * 2
        
        # Create the alphabet sequence
        forward_seq = [chr(65 + j) for j in range(i)]  # A, B, C, ...
        backward_seq = forward_seq[:-1][::-1]  # A, B, ... and then reversed
        
        # Combine forward and backward sequence
        row = forward_seq + backward_seq
        
        # Print the row with spaces
        print(spaces + '   '.join(row))

# Example usage
alphabet_pattern_for_loop(3)

