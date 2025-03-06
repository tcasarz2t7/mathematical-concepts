import math

def find_nth_fibonacci(n):
    if n <= 1:
        return n
    else:
        return find_nth_fibonacci(n-1) + find_nth_fibonacci(n-2)

print(find_nth_fibonacci(7))
