#3Dividing a circle in areas


import math

print("""
   In geometry, the problem of dividing a circle into areas by means of an inscribed polygon with n sides in such a way as to maximise the number of areas created by the edges and diagonals, sometimes called Moser's circle problem""","\n","\n")

n=int(input("N : "))
print("""
n   An
1   1
2   2
3   4""")

if n>=4:
    for i in range(4,n+1):
        ane=(math.factorial(i))*((1/(math.factorial(i-4)*24))+(1/(math.factorial(i-2)*2)))+1
        print(i,end="   ")
        print(round(ane))
