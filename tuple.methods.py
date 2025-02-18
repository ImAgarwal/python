# Empty Tuple
a = ()
print(type(a))


mates = ("Khushi", 22, "Sanskar", 14.5, True, 22 )
print(type(mates))
num = mates.count(22)
print(num)
print(mates.count(14))
a = mates.index(22)
print(a)

print("Sanskar" in mates)
print(14.5 in mates)

print(len(mates))