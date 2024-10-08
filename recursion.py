def compute_factorial(n):
    if n <= 1:
        return 1
    
    return n * compute_factorial(n-1)

def fibonacci_seqence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_seqence(n-1) + fibonacci_seqence(n-2)

def power_of_three(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    
    if n % 3 == 0:
        return power_of_three(n//3)
    
    return False

def reverse_string(n):
    if len(n) == 0 or len(n) == 1:
        return n
    
    return reverse_string(n[1:]) + n[0]
    