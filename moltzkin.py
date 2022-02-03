#1MOTZKIN NUMBERS

print("In mathematics, the nth Motzkin number is the number of different ways of drawing non-intersecting chords between n points on a circle (not necessarily touching every point by a chord). The Motzkin numbers are named after Theodore Motzkin and have diverse applications in geometry, combinatorics and number theory","\n","\n")

def mot(n) :
	
	# Base Case
	if (n == 0 or n == 1) :
		return 1.0

	# Recursion
	else:
		an=((2 * n + 1) * mot(n - 1) + (3 * n - 3) * mot(n - 2)) / (n + 2)
		return an

# Driver code
n = int(input("N : "))
print("\n""n   An")
for i in range(n):
	print(i,end="   ")
	print(mot(i))