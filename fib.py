def fib(count):
    f = [0, 1]
    for i in range(2, count + 1):
        a = f[i - 1] + f[i - 2]
        f.append(a)
    return f[len(f) - 1]
print (fib(10))
