def binary_sum(string1, string2):

    decimal1 = 0
    decimal2 = 0
    string1_reverse = string1[:: -1]
    string2_reverse = string2[:: -1]
    final_string = ''
    
    for i in range(0, len(string1)):
        decimal1 += int(string1_reverse[i]) * pow(2, i)
    
    for i in range(0, len(string2)):
        decimal2 += int(string2_reverse[i]) * pow(2, i)

    sum = decimal1 + decimal2

    while sum > 1:
        final_string += str(sum % 2)
        sum //= 2
    
    return f'1{final_string[::-1]}'
    
print(binary_sum('1101', '101'))

