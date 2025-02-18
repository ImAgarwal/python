f = open("file.txt")

# #readlines reads multiple line (all line in txt)
# # lines = f.readlines()
# # print(lines, type(lines))

# # this read single line
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line1))

# line3 = f.readline()
# print(line3, type(line1))

# line4 = f.readline()
# print(line4, type(line1))

# #THERE is only 4 lines in file.txt and if we try to print fifth line then it doesn't print anything 
# # line5 = f.readline()
# # print(line5, type(line1))

# line5 = f.readline()
# print(line5 == "")   #it asking is fifth line is empty? if yes then it print True else False

# so now there is one more way to write above code
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()