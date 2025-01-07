def generate_fibonacci(n):
    if n <= 0:
        return []  # No Fibonacci numbers for non-positive input
    if n == 1:
        return [0]  # Only the first Fibonacci number
    # Initializing the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Adding the next number
    return fib_sequence

n = 10  # Testing with any number of terms
print(f"First {n} Fibonacci numbers:", generate_fibonacci(n))

