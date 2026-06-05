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