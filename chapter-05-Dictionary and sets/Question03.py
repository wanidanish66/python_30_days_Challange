# this is a program to demonstrate the behavior of sets in Python

s = set()

print(len(s))  # the length of the set is 0

s.add(20)
s.add(20.0)
s.add("20")

print(s)  # the set contains 20, 20.0, and "20"
print(len(s))  # the length of the set is 2, because 20 and 20.0 are considered the same element in a set