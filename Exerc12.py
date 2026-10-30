# Write code that returns the elements common to two lists of integers

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common = []
for a in list1:
    for b in list2:
        if a == b:
            common.append(a)

print("Common elements:", common)