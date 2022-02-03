#Primes Under N
print("A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.","\n","\n")

high= int(input("N : "))
for i in range(1, high+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)