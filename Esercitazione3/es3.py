user_list = input("insert a list that elements are separeted with comma or space\n")
elements = user_list.split()

elements = [int(element) for element in elements]
new_list = []
for a in elements:
    if elements.index(a) % 2 == 0:
        new_list.append(a)
print(new_list)