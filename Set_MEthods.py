#union() function returns unique elements in from both sets
a = set([1, 2, 3, 5]) # or a = {1, 2, 3, 5} Both are same
b = {2, 4, 3, 6, 1}
u = a.union(b)
print("Union:", u)

#intersection() function returns common elements from both sets
c = {"Geek", "for", "Geeks"}
d = {"Computer", "AI", "Geek"}
i = c.intersection(d)
print("Intersection:", i)

#difference() function returns a set containing elements that are in the first set but not in the second
a = {1, 2, 3, 5}
b = {2, 3, 4}
d = a.difference(b)
print("Difference:",d)

#clear() function removes all elements from a set, leaving it empty.
s = {1, 3, 5, 7, 9}
print(s)
s.clear()
print("After clear():", s)