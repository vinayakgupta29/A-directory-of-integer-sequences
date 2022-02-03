#3x+1 Conjectue
print("""The Collatz conjecture or 3x + 1 problem in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one. It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.

The conjecture is named after Lothar Collatz, who introduced the idea in 1937, two years after receiving his doctorate. It is also known as the 3n + 1 problem, the 3n + 1 conjecture, the Ulam conjecture (after Stanisław Ulam), Kakutani's problem (after Shizuo Kakutani), the Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse), or the Syracuse problem. The sequence of numbers involved is sometimes referred to as the hailstone sequence or hailstone numbers (because the values are usually subject to multiple descents and ascents like hailstones in a cloud),or as wondrous numbers.

Paul Erdős said about the Collatz conjecture: "Mathematics may not be ready for such problems." He also offered US$500 for its solution. Jeffrey Lagarias stated in 2010 that the Collatz conjecture "is an extraordinarily difficult problem, completely out of reach of present day mathematics.""", "\n","\n")





n=int(input("N : "))
print("""

""")
print(float(n),"\n"" ↓")
while n!=1:
    if n%2==0 :
        n/=2
        print(n)
        if n!=1:
            print(" ↓ ")
    else:
        n=3*n+1
        print(float(n))
        if n!=1:
            print(" ↓ ")
