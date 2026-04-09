#DataType: List
#Ordered & Mutable
li = ["Chirag", "Saurav", "Kishan"]
for x in li:
    print(x)
    
print("")

#DataType: Tuple
#Ordered & Immutable    
tup = (1, 2, 3, 4, 5, 5)
# tup.append(6) Doesn't allow mutation
for x in tup:
    print(x)

print("")   

#DataType: String
#Ordered & Immutable
strg = "CHIRAG"
for x in strg:
    print(x)
print(f"String - {strg[0]}") #For checking string index
    
print("")

#DataType: Set
#Unordered, Mutable and doesn't allow duplicates
set1 = {29, 28, 29, 27, 24, 27}
for x in set1:
    print(x)

print("")

#DataType: Dictionary
d = {"name" : "Chirag", "age" : 27, "City" : "PBR"}
for key,value in d.items():
    print(f"{key} - {value}")