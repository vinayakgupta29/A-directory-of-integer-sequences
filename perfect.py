#Perfect Numbers
print("In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.","\n","\n")


def perf(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i

    return sum==n

n=int(input("N : "))

for i in range (1,n):
    if perf(i):
        print(i)
