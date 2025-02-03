fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

slicedname = fname[0:3]
    
fullname = fname + " " + lname
greeting = "Greeting Message: Hello {0}! Welcome. You are {1} years old."

print("Full Name: ", fullname)
print("Sliced Name: ", slicedname)
print(greeting.format(slicedname, age))