def compute_factorial(n):
    if n <= 1:
        return 1
    
    return n * compute_factorial(n-1)

def fibonacci_seqence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    