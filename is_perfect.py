def is_perfect(num):
    s = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            s += i
    return s == num

print(is_perfect(6))
print(is_perfect(1))
print(is_perfect(28))
print(is_perfect(33))

