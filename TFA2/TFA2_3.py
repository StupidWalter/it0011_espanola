lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
contact = input("Enter your contact number: ")
course = input("Enter your course: ")

f=open("TFA2\students.txt", "w")
if True:
    f.write("Last Name: " + lname + "\n")
    f.write("First Name: " + fname + "\n")
    f.write("Age: " + age + "\n")
    f.write("Contact Number: " + contact + "\n")
    f.write("Course: " + course)
    print("Students information has been saved to 'students.txt'")
else:
    print("Students information unsuccesfully saved")
    
f.close