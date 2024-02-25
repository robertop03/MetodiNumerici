def prod(a, b):
    c = a * b
    if c < 1000:
        return c
    else:
        c = a + b
        return c

print(prod(3, 5))
print(prod(5, 500))