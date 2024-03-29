# Lists in python
# A built data type that stores set of values
# it can store elements of different types(integer,float,string,etc)

marks = [33,88,44,"string",4.5,True,83,99]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[2])


# List is mutable in python
# Exaple
marks[0] = "irfan"
marks[1] = 33.5

# Sring is immutable it generates error
# Example 

#  str = "string"
# str[0] = "8"
# print(str)

# List slicing 
# Similar to string slicing

str = [44,99,333,848,99]
print(str[1:5])
print(str[:5])
print(str[1:])
print(str[:len(str)])
print(str) # original can't be changed


# negative indexing
str = [38,"hello",38.5]
print(str[-3:-1])





# List Methods
# 1. append()
List = [2,1,3]
# adds one element at the end
print(List.append(4)) # it will print None value 
print(List) # origin list will change

# 2. sort()
# sorting in ascending order
print(List.sort()) # it will print None value 
print(List) # origin list will change

# 3. sort(reverse=True)
# sorting in descending order
print(List.sort(reverse=True)) # none value
print(List)
str1 = ['a','l','b','f','c']
str1.sort()
print(str1)
str1.sort(reverse=True)
print(str1)


# 4. List.reverse()
str1.reverse()
print(str1) # reverse list


# 5. List.insert(idx,el) 
# insert element at particular index
str1.insert(1,'m')
print(str1)


# 6. List.remove()
# removes first occurrence of element

str2 = [1,3,7,1,5]
print(str2.remove(1)) # output is none
print(str2) # first 1 element will remove in list



# 7. list.pop(idx)
# remove element at idx
str2.pop(3)
print(str2)


# Tuples in python
# A built in data type that lets us create immutable sequences of values
tup = (88,90,38,77,55,) # in tupple we can create , in last but its a choice
list = [84,28,77,99]

print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])

#tup[0] = 50 # its a immutable like a string methadology
print(tup)
tuple = ()
print(tuple)
print(type(tuple))

tupp = (1) # its not a tupple and python recive as a integer
print(tupp, type(tupp)) # output is integer number

tupp = (1,) # now its a tupple and python recive as a tupple
print(tupp, type(tupp)) # output is tupple number with type of tupple


# In List 
list = [] # its also a tupple
print(list)
print(type(list))
list1 = [1] # its also a tupple
print(list1)
print(type(list1))


# slicing in tupple
tuple = [2,8,4,0,3]
print(tuple[2:4])



# Methods of Tupple
# 8. tup.index(el) 
# returns index of first occurence

tup = (38,44,99,33,44)
index = tup.index(44) # returns index of first occurence
print(index)


# 9. tup.count(el)
# counts total occurence
print(tup.count(44))



# Lets practise Questions
# QNO 1: WAP to ask the user to enter names of their 3 
# favorite movies and store them in a list.

movies = []
movies.append(input("First movie : "))
movies.append(input("Second movie : "))
movies.append(input("Third movie : "))

print(movies)

# QNO 2: WAP to check if a list contains a palindrom of elements. (Hint: use copy() method)
# ANS :

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("list is palindrom")
else:
    print("list is not palindrom")


copy_list2 = list2.copy()
copy_list2.reverse()

if(list2 == copy_list2):
    print("list is palindrom")
else:
    print("list is not palindrom")




# QNO 3: WAP to count the number of students with the "A" grade in the following tuple?
# ANS:

grade = ("C","D","A","A","B","B","A",)
print('Grade "A" students are : ',grade.count("A"))



# QNO 4: Store the above values in a list & sort them from "A" to "D"?
# ANS:

list = ["C","D","A","A","B","B","A"]
list.sort()
print("List in ascending foram")
print(list)

list.sort(reverse=True)
print("List in discending foram")
print(list)






