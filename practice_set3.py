from datetime import datetime
# Q.1
name = input("Enter your name: ")
print(f"Good Afternoon! {name} Have a nice day!")

#q.2
today_date = datetime.now()
format_date = today_date.strftime("%A, %d-%m-%Y")

letter = '''Dear <|name|>,
You are selected!!! 
<|date|>'''
letter2 = (letter.replace("<|name|>", name).replace("<|date|>", format_date))
print(letter2)

#Q.3

line = '''Twinkle, twinkle,  little star,
How I wonder what you  are!
Up above  the world  so high,
Like a  diamond in  the sky.'''
print((line.find("  ")))
print((line.count("  ")))
# Q.4
print((line.replace("  ", " ")))

letter = '''Dear Harry!!!\n\t This course is nice...\n Thanks!!'''
print(letter)