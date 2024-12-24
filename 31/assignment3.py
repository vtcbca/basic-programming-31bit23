3.def fibonacci_for_loop(terms):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(terms):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
print(fibonacci_for_loop(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

