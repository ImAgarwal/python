
friends = ["Fluffy", 23.5, False, 8, "Apple"]
print(type(friends))
print(friends)
friends[0] = "Boba"  #replace values -- original list chnges
print(friends[0:3])  #slicing done just like strings
 
 #methods
friends.append("Khushi")   # append add value in the end index of the list 
print(friends)
friends.insert(3, "hehehe")   # insert add value at paticular given index 
print(friends)

print(friends.pop(3))  # delete element at index 3 and return its value
print(friends)

l1 = [34, 1, 545, 8, 22, -7]
l1.reverse()
print(l1)
l1.sort() #sort in ascending order
print(l1)
l1.reverse() # reverse sorted list -- chng in descending order
print(l1)