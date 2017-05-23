def bits_to_flip(a, b):
    if a is None or b is None:
        raise TypeError('a or b cannot be None')
    count = 0
    c = a ^ b
    while c:
        count += c & 1
        c >>= 1
    return count


a = int('11101', base=2)
b = int('01111', base=2)
print(bits_to_flip(a, b))
