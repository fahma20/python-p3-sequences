#!/usr/bin/env python3
def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    elif length == 2:
        print("[0, 1]")
        return
    
    # Initialize the list for Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci numbers from the 3rd number to the required length
    for i in range(2, length):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    # Print the Fibonacci sequence
    print(f"{fibonacci_sequence}")

# Example usage
print_fibonacci(0)   # Output: []
print_fibonacci(1)   # Output: [0]
print_fibonacci(2)   # Output: [0, 1]
print_fibonacci(5)   # Output: [0, 1, 1, 2, 3]
print_fibonacci(10)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
