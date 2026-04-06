# Dictionaries

# 1. create a dictionary
dict1 = {"name": "John", "age": 30, "city": "New York"}
dict2 = {"name": "John", "age": 30, "city": "New York"}
dict3 = {"name": "John", "age": 30, "city": "New York"}

print(dict1)
print(dict2)
print(dict3)

# 2. print the dictionary
print(len(dict1))
print(len(dict2))
print(len(dict3))

# 3. indexing
print(dict1["name"])
print(dict1["age"])
print(dict1["city"])

# 4. indexing
dict1["name"] = "John Doe"
dict1["age"] = 31
dict1["city"] = "New York"
print(dict1)

# 5. delete index
del dict1["name"]
del dict1["age"]
print(dict1)

# 6. for loop
for i in dict1:
    print(i)
    
# 7. for loop 
for i in dict1:
    print(i)    
    dict1[i] = dict1[i] + 10
    

# 8. for loop 
for i in dict1:
    print(i)    
    dict1[i] = dict1[i] + 10
    

# 9. for loop 
for i in dict1:
    print(i)






