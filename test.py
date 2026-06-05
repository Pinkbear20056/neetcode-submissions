import string
# python3 test.py

# contains_duplicate example test
# 1
num = [1,1,2,3,4]
uniques = set(num)
print(uniques)

# 2
set_ex = {1,4}
set_ex.add(5)
print(set_ex) # {1, 4, 5}
set_ex.remove(4)
print(set_ex) 
print(len(set_ex))

# 3
nums = [1,1,2,3,4]
first = set(nums)
second = {1,5}

print(first | second) # or {1, 2, 3, 4, 5}
print(first & second) # and {1}
print(first - second) # only first {2, 3, 4}
print(first ^ second) # no in union {2, 3, 4, 5}

if 1 in first:  # if it is in the "first" set
  print("yes")

# 4
my_list = ["apple", "banana", "cherry", "apple"]
my_set = set(my_list)
print(my_set)

# 5
existing_set = {"orange", "mango"}
my_list = ["kiwi", "apple", "apple"]

existing_set.update(my_list)
print(existing_set)

# Valid Anagram
# 1
course = "Python"
print(len(course))  # 6
print(course[0])  # P
print(course[-1]) # n
print(course[0:3])  # Pyt
print(course[0:]) # Python
print(course[:3]) # Pyt
print(course[:])  # Python

# 2
course = "Python \nProgramming"
print(course)
#Python 
#Programming

# 3
first = "Yujin"
last = "Song"
full = first + " " + last
print(full) # Yujin Song
full2 = f"{first} {last}"
print(full2)  # Yujin Song
full3 = f"{len(first)} {2+4}"
print(full3)  # 5 Song

# 4
course1 = "Python programming"
print(course1)
print(course1.upper())  #PYTHON PROGRAMMING
print(course1.lower())  #python programming
print(course1.title())  #Python Programming
print(course1.find("g"))  #10
print(course1.find("G"))  #-1
print(course1.replace("g", "j"))  #Python projramminj
print("pro" in course1) #True
print("swift" not in course1) #True

# 5
# For lowercase: ['a', 'b', ..., 'z']
alphabet_list = list(string.ascii_lowercase)
print(alphabet_list)

# For uppercase: ['A', 'B', ..., 'Z']
uppercase_list = list(string.ascii_uppercase)
print(uppercase_list)

