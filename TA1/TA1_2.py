total_digit = 0
digit = "1234567890"

string_a = input("Enter any word or anything: ")

for char in string_a:
    if char in digit:
        total_digit += int(char)
        
print("Sum of all digits in the String", string_a, ": ",total_digit)