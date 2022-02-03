#3Cake numbers 

print("In mathematics, the cake number, denoted by Cn, is the maximum number of regions into which a 3-dimensional cube can be partitioned by exactly n planes. The cake number is so-called because one may imagine each partition of the cube by a plane as a slice made by a knife through a cube-shaped cake.","\n","\n")


import math
n=int(input("N : "))



    
print("\n""n   An")

if n>=4:
    for i in range(1,n+1):
        ane=(1/6)*(i+1)*((i**2)-i+6)
        print(i, end="   ")
        print(round(ane))

