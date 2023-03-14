def sum_of_square_digits(n):
    sum = 0
    for char in str(n):
        sum += pow(int(char), 2)
    return sum

def is_happy_number(n):
    count = 0
    while count <= 10:
        if sum_of_square_digits(n) == 1:
            return True
        else:
            n = sum_of_square_digits(n)
        count += 1
    return False

print(is_happy_number(7))
    