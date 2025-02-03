f=open("TFA2\students.txt", "r")
if True:
    print("Reading Student Information:")
    for char in f:
        print(char, end = "")
else:
    print("Students information unsuccesful to open")
    
f.close