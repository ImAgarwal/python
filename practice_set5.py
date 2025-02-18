#q.1
means = {"suraj": "Sun", "chand": "Moon", "sitaara" : "Star", "prathavi": "Earth"}
print("suraj, chand, sitaara, prathavi")
word = input("Enter one of the above word to know its english name: ")
print(means[word])


#q.2
nums = set()
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
n = input("Enter your number: ")
nums.add(n)
print(nums)


#q.3
same = {18, "18"}
print(same)

#q.4
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

#q.5
s ={}  
print(type(s))

#q.6, 7, 8
friend = {}
name = input("Enter your name: ")
lang = input("Name your favorite programming language: ")
friend.update({name : lang})
name = input("Enter your name: ")
lang = input("Name your favorite programming language: ")
friend.update({name : lang})
name = input("Enter your name: ")
lang = input("Name your favorite programming language: ")
friend.update({name : lang})
name = input("Enter your name: ")
lang = input("Name your favorite programming language: ")
friend.update({name : lang})

print(friend)

#q.9
s = {8, 7, 12, "Harry", [1, 2]}   # this gives an error becoz list are mutable, and set are inmutable means we can't chng the values in set but we chnge values in list.. thats why we can't put list inside the set 
print(s)
s = {8, 7, 12, "Harry", (1, 2)}  # but we can put tuple inside the sets becoz tuple are also inmutable
print(s)