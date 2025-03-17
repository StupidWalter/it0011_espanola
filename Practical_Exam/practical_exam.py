word_list = []
word_counter = []

string_statement = input("Enter a String Statement: ")
word = string_statement.split()
exclude = ["and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"]
total_word_filter = 0

i = 0
while i < len(word):
    temp_word = word[i]
    temp_word_lower = temp_word.lower()
    
    if temp_word_lower not in exclude:
        if temp_word not in word_list:
            word_list.append(temp_word)
            word_counter.append(1)
            total_word_filter += 1
        else:
            index = 0
            while index < len(word_list):
                if word_list[index] == temp_word:
                    word_counter[index] += 1
                    total_word_filter += 1
                    break
                index += 1
    i += 1
    
word_lower = []
word_upper = []

i = 0
while i < len(word_list):
    if word_list[i][0].islower():
        word_lower.append(word_list[i])
    else:
        word_upper.append(word_list[i])
    i += 1

word_lower.sort()
word_upper.sort()

i = 0
while i < len(word_lower):
    temp_count = word_list.index(word_lower[i])
    print(word_lower[i], "-", word_counter[temp_count])
    i += 1

i = 0
while i < len(word_upper):
    temp_count = word_list.index(word_upper[i])
    print(word_upper[i], "-", word_counter[temp_count])
    i += 1
    
print("Total words filtered: ", total_word_filter)