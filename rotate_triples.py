def rotate_left (triple):
  (a, b, c) = triple
  new_triple_left = (b, c, a)
  return new_triple_left

def rotate_right (triple):
  (a, b, c) = triple
  new_triple_right = (c, a, b)
  return new_triple_right
  
triple = (1, 2, 3)

print(triple)
print(rotate_left(triple))
print(rotate_right(triple))