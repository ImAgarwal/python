empty_set = set()    # Don't use set = {} as it will create an empty dictionary.
s = {1, 2, 3, 46, 3, 3,51, "Sam"}
s.add(566)
print(s) 
s.remove(1)
print(s) 
print(type(list(s)) )   

# Union and intersection
s1 = {1, 34, 78, 34, 56, 2}
s2 = {1, 23, 45, 78, 89, 34}

print(s1.union(s2))      # combine both and remove repeated value

print(s1.intersection(s2))  # only print repeated value in both sets

# subset and superset
print({1, 2}.issubset(s1))   #  in simple it means is 1 and 2 is a part of s1 or not
print(s1.issuperset({1, 56}))  # it simply means is s1 contains 1 and 56 or not                                    

ert = set()
ert.add(18)
ert.add("18")
ert.add(18.00)
print(ert)