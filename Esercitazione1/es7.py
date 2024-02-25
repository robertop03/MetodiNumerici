import numpy as np
def do_things(lista):
    print(sum(lista))
    array = np.array(lista)
    print(np.prod(lista))

def product_or_sum(lista, sum_yes):
    if sum_yes:
        print(sum(lista))
    else:
        array = np.array(lista)
        print(np.prod(lista))

do_things([1, 3, 4])
product_or_sum([1, 3, 4], False)
product_or_sum([1, 3, 4], True)