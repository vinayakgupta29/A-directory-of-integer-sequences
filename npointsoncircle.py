import math
print("If n points points on the circumferemce ")
num=int(input("N : "))

print("\n""n   An")
for i in range(num+1):
  a= math.comb(i,2)
  print(i, end="   ")
  print(a)