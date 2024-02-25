def check_string(str1, str2):
    for char in str1:
        if char not in str2:
            return False
    return True
print(check_string("by", "blueberry"))
print(check_string("byZ", "blueberry"))