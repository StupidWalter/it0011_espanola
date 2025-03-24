def divide (a, b):
    if b == 0:
        return None
    return a / b

def exponentiation (a, b):
    return a ** b

def remainder (a, b):
    if b == 0:
        return None
    return a % b

def summation (a, b):
    c = 0
    while a != b+1:
        c += a
        a += 1
    return c

def portal(choice, a, b):
    if choice == "D":
        c = divide(a, b)
        if c is not None:
            print(f"\n{a} / {b} = {c}\n")
        else:
            print("\nThe second number or denominator must not be equal to zero. \n")
        
    elif choice == "E":
        print(f"\n{a} ** {b} = {exponentiation(a, b)}\n")
        
    elif choice == "R":
        c = remainder(a, b)
        if c is not None:
            print(f"\n{a} % {b} = {c}\n")
        else:
            print("\nThe second number or denominator must not be equal to zero. \n")
    
    elif choice == "F":
        if a < b:
            print(f"\n{b - a + 1}∑{a} = {summation(a, b)}\n")
        else:
            print("\nSecond number must be greater than the first number. \n")
        
    else:
        print("\nUnexpected Error. \n")

running = True
while running == True:
    print("[D] - Divide ")
    print("[E] - Exponentiation ")
    print("[R] - Remainder ")
    print("[F] - Summation ")
    print("[Q] - Quit ")
    choice = input("Enter your choice: ").upper()
    
    if choice == "Q":
        running = False
        
    elif choice in ["D", "E", "R", "F"]:
        try:
            a = int(input("Input 1st Number: "))
            b = int(input("Input 2nd Number: "))
        except ValueError:
            print("\nIntegers only. \n")
            continue
    
        portal(choice, a, b)

    else:
        print("\nThere is no such choice. \n")
