def encrypt (string):
    l = list(string)
    for i in range(0, len(string) - 1, 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    return ''.join(l)

print(encrypt("move")) # 'omev'
print(encrypt("attack")) # 'taatkc'
print(encrypt("go!")) # 'og!'