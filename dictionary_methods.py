empty_dict = {} # this will create empty dictionary

marks = {"Harry": 99,
         "Khushi": 100,
         "Shubham": 56,
         "Roohi": 43,
         'ghare': 'yok',
         "lists": [1, 2, 3]}
print(marks["Khushi"]) # gives error if the key is not in dictionary
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 88, "Faye": 69})
print(marks["Faye"])
print(marks.get("Roohi")) # get() - works same as marks["Roohi"] but 
print(marks.get("Yoko")) #get()- if key is not in dictionary, returns None
print(marks.get('animal', 'bunny'))
print(marks.pop('ghare')) # Removes the specified key and returns its value
print(marks.popitem()) # Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.
new_marks = marks.copy()
marks.clear()
print("After clearing : ", marks)
print(new_marks)