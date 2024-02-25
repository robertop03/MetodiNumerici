a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for a_element in a:
    if a_element in b and not a_element in c:
        c.append(a_element)
print(c)