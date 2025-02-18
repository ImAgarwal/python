f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# the same can be written using  'with' statement like this:
with open("file.txt") as f:
    print(f.read())
# u don't have to explicitly close the file it close automatically


#if u open file.txt in write mode and write in it then it clear all previous data before rewrite new data
st = "Hey anyogaseeyo hohohoo 123 89.45"
f1 = open("file2.txt", "w")
f1.write(st)
f1.close()


