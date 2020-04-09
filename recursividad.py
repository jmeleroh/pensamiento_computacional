def factorial(n):
    if n== 1:
        return 1
    print(n)
    
    return n * factorial(n - 1)





n = int(input('Dame un número: '))

print(factorial(n))


