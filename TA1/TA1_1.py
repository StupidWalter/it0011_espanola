vowel = "aeiou"
consonant = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

count_vowel = 0
count_consonant = 0
count_space = 0
count_other = 0

string_a = input("Enter any word or anything: ")

for char in string_a:
    if char in vowel:
        count_vowel += 1
    elif char in consonant:
        count_consonant += 1
    elif char == " ":
        count_space += 1
    else:
        count_other += 1

print("Count of vowels, consonant, space and others in the string", string_a, ": ")
print("Vowels: ", count_vowel)
print("Consonant: ", count_consonant)
print("Space: ", count_space)
print("Others: ", count_other)   