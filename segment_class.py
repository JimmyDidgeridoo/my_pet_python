def is_degenerated(line):
    (x1, y1, x2, y2) = line
    return x1 == x2 and y1 == y2

def is_vertical(line):
    (x1, y1, x2, y2) = line
    return x1 == x2 and y1 != y2

def is_vertical(line):
    (x1, y1, x2, y2) = line
    return x1 == x2 and y1 != y2

def is_horizontal(line):
    (x1, y1, x2, y2) = line
    return x1 != x2 and y1 == y2

def is_horizontal(line):
    (x1, y1, x2, y2) = line
    return x1 != x2 and y1 == y2

def is_inclined(line):
    (x1, y1, x2, y2) = line
    return x1 != x2 and y1 != y2

line1 = (0, 10, 100, 130)
print(is_vertical(line1))  # False
print(is_horizontal(line1))  # False
print(is_degenerated(line1))  # False
print(is_inclined(line1))  # True
line2 = (42, 1, 42, 2)
print(is_vertical(line2))  # True
line3 = (100, 50, 200, 50)
print(is_horizontal(line3))  # True



