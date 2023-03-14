def is_power_of_three(n):
    i = 1
    while i < n:
        i *= 3
    return i == n

print(is_power_of_three(8))
print(is_power_of_three(243))
