set_a = {'a', 'g', 'b', 'c', 'd', 'f'}
set_b = {'l', 'm', 'o', 'b', 'c', 'h'}
set_c = {'k', 'i', 'j', 'h', 'c', 'd', 'f'}

question_a = set_a.union(set_b)
print("A. How many elements are there in set A and B: ", len(question_a))

question_b = set_b.difference(set_a.union(set_c))
print("B. How many elements are there in B that is not part of A and C", len(question_b))

print("C. Show the following using set operations: ")

question_c1 = set_c.difference(set_a)
print("i.", question_c1)

question_c2 = set_a.intersection(set_c)
print("ii.", question_c2)

question_c3 = set_a.intersection(set_b).union(set_b.intersection(set_c))
print("iii.", question_c3)

question_c4 = set_a.intersection(set_c).difference(set_b)
print("iv.", question_c4)

question_c5 = set_a.intersection(set_b.intersection(set_c))
print("v.", question_c5)

question_c6 = set_b.difference(set_a.union(set_c))
print("vi.", question_c6)