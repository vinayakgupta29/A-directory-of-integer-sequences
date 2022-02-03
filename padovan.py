#Padovan Sequence
print("The Padovan sequence is named after Richard Padovan who attributed its discovery to Dutch architect Hans van der Laan in his 1994 essay Dom. Hans van der Laan : Modern Primitive. The sequence was described by Ian Stewart in his Scientific American column Mathematical Recreations in June 1996. He also writes about it in one of his books, Math Hysteria: Fun Games With Mathematics.","\n","\n")


a=1
b=1
c=1
n=int(input("N: "))
print("""
n   An
1   1
2   1
3   1""")
#sequence code
for i in range(n+1):
    Pn=(b+a)
    print(i+4, end="   ")
    print(Pn,"\n")
    #updating values
    a=b
    b=c
    c=Pn