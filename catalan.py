#2CATALAN NUMBERS

import math

print("""In combinatorial mathematics, the Catalan numbers are a sequence of natural numbers that occur in various counting problems, often involving recursively defined objects. They are named after the French-Belgian mathematician Eugène Charles Catalan (1814–1894).""","\n","\n")

n=int(input("N : "))
print("\n""n   An")

for i in range (n+1):
    an=math.factorial(2*i)/(math.factorial(i+1)*math.factorial(i))
    print(i,end="   ")
    print(an)

