
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
