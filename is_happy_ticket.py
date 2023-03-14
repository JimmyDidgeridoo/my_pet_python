def is_happy_ticket(string):
    
    if len(string) % 2 != 0:
        return False
    else:
        s1 = 0
        s2 = 0    
        str1 = string[0 : int(len(string) / 2)]
        str2 = string[int(len(string) / 2) :]
        for char in str1:
            s1 += int(char)
        for char in str2:
            s2 += int(char)
        return s1 == s2

print(is_happy_ticket('123123')) # True
print(is_happy_ticket('341800')) # True
print(is_happy_ticket('42')) # False
print(is_happy_ticket('12345678')) # False
