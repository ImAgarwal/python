
#q.1
fruits = []
input("Enter friuts name: ")
f1 = input("1- ")
fruits.append(f1)
f2 = input("2- ")
fruits.append(f2)
f3 = input("3- ")
fruits.append(f3)
f4 = input("4- ")
fruits.append(f4)
f5 = input("5- ")
fruits.append(f5)
f6 = input("6- ")
fruits.append(f6)
f7 = input("7- ")
fruits.append(f7)
print(fruits)

# q.2
marks = []
input("Enter students marks: ")
f1 = int(input("Student 1- "))
marks.append(f1)
f2 = int(input("Student 2- "))
marks.append(f2)
f3 = int(input("Student 3- "))
marks.append(f3)
f4 = int(input("Student 4- "))
marks.append(f4)
f5 = int(input("Student 5- "))
marks.append(f5)
f6 = int(input("Student 6- "))
marks.append(f6)
marks.sort()
print(marks)

# q.3
a = ("Harry", 23.5, 812)
a[0] = "Larry"

# q.4
list = [1, 2, 3, 4, 5]
print(sum(list))  #sum() - built-in function for adding
print(max(list))
print(min(list))

# q.5
t = (7, 0, 8, 0, 0, 9)
print(t.count(0))