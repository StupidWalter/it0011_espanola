integer_a = int(input("Enter any number for a: "))
integer_b = input("Enter any number for b: ")

print("a: ")
for integer in range(1, integer_a+1):
    counter_a = 0
    while counter_a < integer:
        counter_a += 1
        print(counter_a, end="")
    print()
    
print("b: ")
for integer in integer_b:
    integer = int(integer)
    counter_b = 0
    while counter_b < integer:
        print(integer, end="")
        counter_b += 1
    print()