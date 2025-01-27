# Methods Todays Class
def box(a,b):
    return a+b
sum = box(6,2)
print(sum)

# Methods Todays Class

name:str = "pakistan"
print(type(name))

name1 = name.capitalize()
print(name.count("a"))
print(len(name))
print(name.find("P"))
print(name1)
print(name)


name: str = "My Name is M Fahad Ahmed My Natonality is Pakistani"
name1 = name.capitalize()
print(name1)
print(name.replace("Pakistani","Sindh KHI").upper())




my_list = ['Shoaib', 'Tariq Mehta', "Zaid",]
my_list.append("Naveed Chacha")
print(my_list)


my_list.insert(0,'Sir Zia')
print(my_list)

my_list.reverse()
print(my_list)


my_list.pop()
print(my_list)


my_list.remove('Shoaib')
print(my_list)


my_list.sort()
print(my_list)

new_teachers = ['Sir Aneeq', 'Sir Ameen']
print('Old List', my_list)
my_list.extend(new_teachers)
print('Updated List', new_teachers)



# Dictionary

new_dic = {
          'Name': 'M FAhad Ahmed',
          'Gender': 'Male',
          'Age' : 43
}

print(new_dic)
# Keys
print(new_dic.keys())
# Values
print(new_dic.values())
# Items
print(new_dic.items())


# Get
print(new_dic.get("Name"))

# Update

new_dic1 = {"city" : "Karachi"}
new_dic2 = {"Country": "Pakistan"}
new_dic.update(new_dic1)
new_dic.update(new_dic2)
print(new_dic1)
print(new_dic2)


# Pop in Dictionary
print(new_dic.pop("Age"))
print(new_dic)


# Clear

new_dic.clear()
print(new_dic)



# ```python
# String Methods
name: str = "pakistan"
name1 = name.capitalize()
print("String capitalize:", name1)  # Capitalizes the first letter of the string
print("Count of 'a':", name.count("a"))  # Counts occurrences of 'a'
print("Length of string:", len(name))  # Length of the string
print("Find 'P' in string:", name.find("P"))  # Finds the first occurrence of 'P'
print("Uppercase version:", name.upper())  # Converts string to uppercase
print("Lowercase version:", name.lower())  # Converts string to lowercase
print("String starts with 'P':", name.startswith('P'))  # Checks if string starts with 'P'
print("String ends with 'n':", name.endswith('n'))  # Checks if string ends with 'n'
print("Replaced string:", name.replace("pakistan", "India"))  # Replaces 'pakistan' with 'India'
print("Split string:", name.split('a'))  # Splits the string at 'a' and returns a list
print("Is all alphabetic:", name.isalpha())  # Checks if all characters are alphabetic
print("Is all digits:", name.isdigit())  # Checks if all characters are digits
print("String with spaces removed:", name.strip())  # Removes any leading or trailing spaces

# List Methods
my_list = ['Shoaib', 'Tariq Mehta', "Zaid"]
print("Original List:", my_list)

# 1. Append
my_list.append("Naveed Chacha")
print("After append:", my_list)

# 2. Insert
my_list.insert(0,'Sir Zia')
print("After insert:", my_list)

# 3. Reverse
my_list.reverse()
print("After reverse:", my_list)

# 4. Pop
my_list.pop()
print("After pop:", my_list)

# 5. Remove
my_list.remove('Shoaib')
print("After remove:", my_list)

# 6. Sort
my_list.sort()
print("After sort:", my_list)

# 7. Extend
new_teachers = ['Sir Aneeq', 'Sir Ameen']
my_list.extend(new_teachers)
print("After extend:", my_list)

# 8. Copy
my_list_copy = my_list.copy()
print("List copy:", my_list_copy)

# 9. Index
index_of_zaid = my_list.index("Zaid")
print("Index of 'Zaid':", index_of_zaid)

# 10. Count
count_of_tariq = my_list.count("Tariq Mehta")
print("Count of 'Tariq Mehta':", count_of_tariq)

# 11. Clear
my_list.clear()
print("After clear:", my_list)

# 12. Slice
my_list = ['Shoaib', 'Tariq Mehta', "Zaid", "Sir Zia"]
print("List slice:", my_list[1:3])

# Tuple Methods
my_tuple = ('Shoaib', 'Tariq Mehta', "Zaid", 'Zaid')
print("Tuple:", my_tuple)
count_of_zaid = my_tuple.count("Zaid")
print("Count of 'Zaid' in tuple:", count_of_zaid)

# Index
index_of_tariq = my_tuple.index("Tariq Mehta")
print("Index of 'Tariq Mehta':", index_of_tariq)

# Dictionary Methods
new_dic = {
    'Name': 'M FAhad Ahmed',
    'Gender': 'Male',
    'Age': 43
}
print("Original Dictionary:", new_dic)

# 1. Keys
print("Keys:", new_dic.keys())

# 2. Values
print("Values:", new_dic.values())

# 3. Items
print("Items:", new_dic.items())

# 4. Get
print("Get 'Name':", new_dic.get("Name"))

# 5. Update
new_dic1 = {"city" : "Karachi"}
new_dic2 = {"Country": "Pakistan"}
new_dic.update(new_dic1)
new_dic.update(new_dic2)
print("Updated Dictionary:", new_dic)

# 6. Pop
print("Pop 'Age':", new_dic.pop("Age"))
print("Dictionary after pop:", new_dic)

# 7. Pop Item
print("Pop last item:", new_dic.popitem())
print("Dictionary after pop item:", new_dic)

# 8. Clear
new_dic.clear()
print("Dictionary after clear:", new_dic)

# 9. Setdefault
new_dic = {'Name': 'M Fahad Ahmed'}
new_dic.setdefault('Age', 30)
print("Setdefault method:", new_dic)

# 10. Fromkeys
new_dict_fromkeys = dict.fromkeys(['a', 'b', 'c'], 10)
print("Fromkeys method:", new_dict_fromkeys)

# 11. Copy
new_dic_copy = new_dic.copy()
print("Copy of dictionary:", new_dic_copy)

# 12. Contains
print("'Name' in dictionary:", 'Name' in new_dic)

# Code Explanation:

# 1. String Methods: 
#   - capitalize(), count(), len(), find(), upper(), lower(), startswith(), endswith(), replace(), split(), isalpha(), isdigit(), strip().
   
# 2. List Methods:
#   - append(), insert(), reverse(), pop(), remove(), sort(), extend(), copy(), index(), count(), clear(), slice().

# 3. Tuple Methods:
#   - count(), index().

# 4. Dictionary Methods:
#   - keys(), values(), items(), get(), update(), pop(), popitem(), clear(), setdefault(), fromkeys(), copy(), contains() (with in operator).
