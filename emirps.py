print("An emirp (prime spelled backwards) is a prime number that results in a different prime when its decimal digits are reversed.[1] This definition excludes the related palindromic primes.")

# This function reverses the given number
def reve(n):
    r = 0
    while (n):
        r = r * 10 + n % 10
        n = int(n / 10)
    return r


# This function checks if a given number is Prime number
def Prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return 0
    return 1



# This function Checks if a number is a Palindrome or not
def Palin(n):
    return (n == reve(n))

n=int(input("N : "))
#Check for emiprs
for i in range(n):
    if Prime(i) and Prime(reve(i)) and not Palin(reve(i)):
        print(i)