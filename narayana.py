#Narayana's Cow Sequence
print("the number of cows present each year, starting from one cow in the first year, where every cow has one baby cow each year starting in its fourth year of life.","\n","\n")



a,b,c=1,1,1
count=0
n=int(input("N: "))
print("""
n   An
""")
for i in range(n+1):
    print(i, end="   ")
    print(a)
    an=c+a
    a=b
    b=c
    c=an
