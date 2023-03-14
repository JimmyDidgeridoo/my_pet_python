def angle_adaptation(angle): #функция приведения угла
    if angle > 360:
        return angle % 360
    elif angle < 0:
        return (abs(angle) // 360 + 1)* 360 + angle
    else:
        return angle

def diff(a, b):
    angle_adaptation(a)
    angle_adaptation(b)
    x = a - b
    y = b - a
    if x < 0:
        x += 360
    if y < 0:
        y += 360
    return min(x, y)

print(diff(0, 45))
# 45
print(diff(0, 180))
# 180
print(diff(0, 190))  # не 190, а 170, потому что 170 меньше
# 170
print(diff(120, 280))
# 160