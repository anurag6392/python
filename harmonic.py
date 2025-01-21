def harmonic_sum(n):
    # Calculate the harmonic sum up to n-1
    return sum(1 / i for i in range(1, n))

# Input: Positive integer n
try:
    n = int(input("Enter a positive integer: "))
    if n <= 1:
        print("n should be greater than 1 to compute H(n-1).")
    else:
        # Calculate and display the harmonic sum
        result = harmonic_sum(n)
        print(f"The harmonic sum H({n-1}) is: {result}")
except ValueError:
    print("Please enter a valid positive integer.")
