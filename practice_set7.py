#q.1
n = int(input("Enter your number for table: "))
for i in range (1, 11):
    print(f"{n} X {i} = {n*i}")

#q.2
l1 = ["Harry", "Sonam","Sachin", "Rahul"]
for i in l1:
    if(i.startswith("S")):
        print(f"Hello!! {i}")

#q.3
n = int(input("Enter your number for table: "))
i=1
while(i<11):
    print(f" X {i} = {i*7}")
    i+=1

#q.4
n = int(input("Enter your number: "))
for i in range(2, n):
    if((n%i)== 0 ):
        print("Your is not a prime number")
        break
else: 
    print("Your number is prime number")


#q.5
n = int(input("Enter your number: "))
sum = 0
i = 1
while(i<= n):
   sum = sum + i
   i += 1
print(sum)

#q.6
n = int(input("Enter your number: "))
fact = 1
for i in range (1, n+1):
    fact = fact * i

print(fact)

#q.7
'''
for n = 3
  *
 ***
*****

'''
n = int(input("Enter your number: "))
for i in range(1, n+1):
    print(" "* (n-i), end= "")  #end="" -- buy using this print statement by defualt doen't add line
    print("*"*(2*i-1), end= "")  #end="" -- buy using this print statement by defualt doen't add line 
    print("\n")

#q.8
'''
for n =3 
*
**
***
'''
n = int(input("Enter your number: "))
for i in range(1, n+1):
    print("*"*i)
#q.9
'''
for n =3
***
* *
***
'''
n = int(input("Enter your number: "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*")

#q.10
n = int(input("Enter your number: "))
for i in range(1, 11):
    print(f"{n} X {(11-i)} = {n*(11-i)}")
