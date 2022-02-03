import os

def choose(choice):
    if choice in ('1','2','3','4','5','6','7','8','9','10','11','12'):
        if choice=='1':
            os.system('cls')
            exec(open("3x+1conj.py").read())
        elif choice=='2':
            os.system('cls')
            exec(open("prime.py").read())
        elif choice == '3':
            os.system('cls')
            exec(open("emirps.py").read())
        elif choice == '4':
            os.system('cls')
            exec(open("perfect.py").read())
        elif choice == '5':
            os.system('cls')
            exec(open("bell.py").read())
        elif choice == '6':
            os.system('cls')
            exec(open("narayana.py").read())
        elif choice == '7':
            os.system('cls')
            exec(open("catalan.py").read())
        elif choice == '8':
            os.system('cls')
            exec(open("cakenum.py").read())
        elif choice == '9':
            os.system('cls')
            exec(open("npointsoncircle.py").read())
        elif choice== '10':
            os.system('cls')
            exec(open("moltzkin.py").read())
        elif choice== '11':
            os.system('cls')
            exec(open("divicircle.py").read())
        elif choice == '12':
            os.system('cls')
            exec(open("padovan.py").read())
    else:
        print("Choose a correct option")
        print(p)

os.system("cls")
print("hello")
p=""" 
        1. 3x+1 Conjecture 
        2. Primes under N
        3. Emirps under N
        4. Perfect Numbers under N
        5. Bell Numbers 
        6. Narayana's Cow Sequence 
        7. Catalan Numbers
        8. Cake Number
        9. Joining N points on a circle
        10. Moltzkin Numbers
        11. Dividing a Circle
        12. Padovan Spiral sequence
        13f. Close
"""

print(p)
while True:
        choice =input("Choice:")
        if (choice=='13f'):
            break
        else:
            choose(choice)
            print("\n","\n")
            ho=input("Bck : ")
            if ho == "y":
                print(p)
                continue
            else:
                choose(choice)
        break
