def palidromer_checker(a):
    return str(a) == str(a)[::-1]

f=open("Technical_Midterm_Exam\\numbers.txt", "r")
if f:
    linecount = int(1)
    for number in f:
        number = number.strip()
        if number:
            sum = int(0)
            print("Line ", linecount, ": ", number, sep = "", end = " ")
            temp_line = ""
            for char in number:
                if char == ",":
                    sum += int(temp_line)
                    temp_line = ""
                else:
                    temp_line += char
            if temp_line:
                sum += int(temp_line)
            if palidromer_checker(sum):
                ispalidrome = "Palindrome"
            else:
                ispalidrome = "Not a Palindrome"
            print("(sum ", sum, ") - ", ispalidrome, sep = "")
            linecount += 1

else:
    print("numbers.txt is unsuccessful to open")

f.close()
