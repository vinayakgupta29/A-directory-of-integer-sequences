#Bell Number
print("""In combinatorial mathematics, the Bell numbers count the possible partitions of a set. These numbers have been studied by mathematicians since the 19th century, and their roots go back to medieval Japan. In an example of Stigler's law of eponymy, they are named after Eric Temple Bell, who wrote about them in the 1930s.""","\n","\n")


def bellNumber(n):

    bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bell[0][0] = 1
    for i in range(1, n + 1):

        # Explicitly fill for j = 0
        bell[i][0] = bell[i - 1][i - 1]

        # Fill for remaining values of j
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    return bell[n][0]


n=int(input("N : "))
# Driver program
for n in range(n):
    print(n,"th Bell Number is",  bellNumber(n))
