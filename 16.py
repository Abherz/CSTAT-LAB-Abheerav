import math

def fibonacci(n):
    
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    return round((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))

n = int(input("Enter n: "))
print(fibonacci(n))