import random
'''
1 for paper
0 for rock
-1 for scissors
'''

# this generates a random no.
computer = random.choice([-1, 0, 1])


user_str = input("Enter your choice: ")

#this covert my string input into int(number)
user_dict = {"p" : 1, "r" : 0, "s" : -1}

#this is for to get number from user_dict acc. to my input 
user = user_dict[user_str]

#this is for to give what number hold what element
name_dict = {1 : "Paper", 0 : "Rock", -1 : "Scissors"}

#this is for to print what u chose and what computer chose 
print(f"You chose {name_dict[user]} and computer chose {name_dict[computer]}")

if(computer == user):
    print("Its a Draw!!!")

else:
    if(computer == 1 and user == 0):
        print("You Lose!!!")
    elif(computer == 0 and user == 1):
        print("You Win!!!")
    elif(computer == -1 and user == 0):
        print("You Win!!!")
    elif(computer == 0 and user == -1):
        print("You Lose!!!")
    elif(computer == -1 and user == 1):
        print("You Lose!!!")
    elif(computer == 1 and user == -1):
        print("You Win!!!")
    else:
        print("Something went wrong")
        