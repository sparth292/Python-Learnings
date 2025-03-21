s1 = "Parth"

print(s1)

print(s1.upper())

print(s1.lower())

print(len(s1))

print(s1.isalpha())  #(contains numbers)
print(s1.isdigit())  
print(s1.isalnum())  #(letters + numbers)

# What is string slicing ? 
# Answer: A string in python can be sliced to get a part of it

print(s1[1:4])  
print(s1[:3])   #  (first 3 characters)
print(s1[3:])   #  (from index 3 to end)
print(s1[::-1]) #  (reverse string)


# Strings in Python are immutable