## 6월 4일 목요일
### contains_duplicate

#### 파이썬에서 가장 대표적인 내장 자료구조 4가지
| 자료구조 | 특징 | 예시 |
|----------|----------|----------|
| `list` | 순서 O, 수정 O, 중복 O | `[1, 2, 3]` |
| `tuple` | 순서 O, 수정 X, 중복 O | `(1, 2, 3)` |
| `set` | 순서 X, 수정 O, 중복 X | `{1, 2, 3}` |
| `dict` | Key-Value 저장 | `{"name": "Yujin", "age": 22}` |


#### set 
: collection with no duplicates

basic example 
```python 
num = [1,1,2,3,4]
uniques = set(num)
print(uniques) # {1,2,3,4}
```

```python 
set_ex = {1,4}
set_ex.add(5)
print(set_ex) # {1, 4, 5}
set_ex.remove(4)
print(set_ex) # {1, 5}
print(len(set_ex)) # 2
```
##### Union
```python
nums = [1,1,2,3,4]
first = set(nums)
second = {1,5}

print(first | second) # or {1, 2, 3, 4, 5}
print(first & second) # and {1}
print(first - second) # only first {2, 3, 4}
print(first ^ second) # no in union {2, 3, 4, 5}

if 1 in first:  # if it is in the "first" set
  print("yes")
```

#### List를 Set으로 전환하고 사용하기
##### Create a New Set from a List
```python
my_list = ["apple", "banana", "cherry", "apple"]
my_set = set(my_list)
print(my_set)
# Output: {'banana', 'apple', 'cherry'} (Order may vary)
```
##### Add List Items to an Existing Set
```python
existing_set = {"orange", "mango"}
my_list = ["kiwi", "apple"]

existing_set.update(my_list)
print(existing_set)
# Output: {'orange', 'mango', 'kiwi', 'apple'}
```

##### 특징
- 순서가 없기 때문에 index로 print 불가능함 
- index를 접근하기 위해서는 list를 써야함

##### 주의사항
`dup = {}`: 빈 dict가 생성 (빈 set가 아님)
`dup = set()`: 빈 set 생성

### Valid Anagram
Anagram 뜻: 문자의 종류와 개수가 모두 같고, 순서만 다른 경우

#### sting 
baisc examples
```python
course = "Python"
print(len(course))  # 6
print(course[0])  # P
print(course[-1]) # n
print(course[0:3])  # Pyt
print(course[0:]) # Python
print(course[:3]) # Pyt
print(course[:])  # Python

course = "Python \nProgramming"
print(course)
#Python 
#Programming

first = "Yujin"
last = "Song"
full = first + " " + last
print(full) #Yujin Song
full2 = f"{first} {last}" # replaced at runtime
print(full2)  #Yujin Song
full3 = f"{len(first)} {last}"
print(full3)  #5 6
```

useful functions
```python
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
```

#### List - 내일 공부 더하기
정렬하는 방법
```python
import string

# For lowercase: ['a', 'b', ..., 'z']
alphabet_list = list(string.ascii_lowercase)

# For uppercase: ['A', 'B', ..., 'Z']
uppercase_list = list(string.ascii_uppercase)
```