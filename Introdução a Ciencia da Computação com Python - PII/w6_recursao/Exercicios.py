def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(5))

#0, 1, 1, 2, 3, 5

def x(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))