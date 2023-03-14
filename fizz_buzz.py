def fizz_buzz(begin, end):
    string = ''
    if begin <= end:
        for i in range(begin, end + 1):
            if i % 3 == 0 and i % 5 == 0:
                string += 'FizzBuzz '
            elif i % 3 == 0:
                string += 'Fizz '
            elif i % 5 == 0:
                string += 'Buzz '
            else:
                string = string + str(i) + ' '
    return string
print(fizz_buzz(11, 20))

