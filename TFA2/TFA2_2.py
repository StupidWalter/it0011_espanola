fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

fullname = fname + " " + lname
fullname_up = fullname.upper()
fullname_low = fullname.lower()
fullname_len = len(fullname)

print("Full Name: ", fullname)
print("Full Name (Upper Case): ", fullname_up)
print("Full Name (Lower Case): ", fullname_low)
print("Length of Full Name: ", fullname_len)