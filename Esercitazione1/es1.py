# data una lista, stampare tutti gli elementi della lista minori di 5.
a = [1, 2, 3, 4, 5, 6, 7, 8]
for el in a:
    if el < 5:
        print(el)

# invece di stampare gli elementi uno per uno, creare una nuova lista che contenga tutti gli elementi inferiori a 5 dall'elenco di input
# e stampare questa nuova lista.
l = []
for el in a:
    if el < 5:
        l.append(el)
print(l)