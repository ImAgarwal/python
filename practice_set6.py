#q.1
nums = [ ]
for i in range(1, 5):
   n = int(input(f"Enter your number {i}: "))
   nums.append(n)

print(max(nums))
# n = int(input("Enter your number 1: "))
# nums.append(n)
# n = int(input("Enter your number 2: "))
# nums.append(n)
# n = int(input("Enter your number 3: "))
# nums.append(n)
# n = int(input("Enter your number 4: "))
# nums.append(n)
# print(max(nums))

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if(n1 > n2 and n1 > n3 and n1 > n4):
    print("Greatest number is ", n1)
elif(n2 > n1 and n2 > n3 and n2 > n4):
    print("Greatest number is ", n2)
elif(n3 > n2 and n3 > n1 and n3 > n4):
    print("Greatest number is ", n3)
else:
    print("Greatest number is ", n4)

#q.2

#q.3
#q.4
#q.5
#q.6