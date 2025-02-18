

#q.1
f = open("file.txt")
content = f.read()
if("Twinkle" in content):
    print("Yes!!!")
else:
    print("Nooo")


#q.2
import random
def game():
    print("You are playing a game...")
    score = random.randint(1, 62)
    #Fetch the hiscore
    with open("hiscore.txt") as f: 
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score > hiscore):
       #write this hiscore to the file
       with open("hiscore.txt", "w" ) as f:
           f.write(str(score)) # we chnge this into str becoz write func only take string

    return score

game() 

#q.3
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 22):
    generateTable(i)

'''
Let's say n is 2 and i is 1 in the first iteration:

Initially, table is "".
After the first iteration, table becomes "2 X 1 = 2\n".
In the second iteration, when i is 2:

The current value of table is "2 X 1 = 2\n".
After the second iteration, table becomes "2 X 1 = 2\n2 X 2 = 4\n".
This process continues until the loop completes, resulting in a complete multiplication table for the number n.
'''

#q.4
word = "donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(contentNew)

#q.5
words = ["donkey", "amazing", "blue", "are"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)


#q.6
with open("log.txt") as f:
    content = f.read()
if("python" in content):
    print("Yes!!!")
else:
    print("Nooo") 

#q.7
with open("log.txt", "r") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if("python" in line):
        print(f"yess!! python is present in line no. {line_no}")
        break
    line_no += 1

else:
    print("No!!! python not present.")


#q.8
with open("file.txt", "r") as f:
    content = f.read()
with open("file_copy.txt", "w") as f:
    f.write(content)

#q.9
with open("file.txt", "r") as f:
    content1 = f.read()
with open("file_copy.txt", "r") as f:
    content2 = f.read()
if(content1 == content2):
    print("Both files are identical.")
else:
    print("Both files are not identical.")

#q.10
with open("file_copy.txt", "w") as f:
    f.write("")

#q.11
with open("old.txt", "r") as f:
    content1 = f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(content)
