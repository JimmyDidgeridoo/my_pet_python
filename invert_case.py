def invert_case(string):
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string

print(invert_case('PyThOn'))