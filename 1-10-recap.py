# a = input('Enter your name: ')

# 4 video content 

# a = 'name'
# b = 23
# c = '30'

# # print(a + b)
# # >> TypeError: can only concatenate str (not "int") to str

# print(a + str(b))
# # >> name23

# # print(int(a) + b)
# # >> ValueError: invalid literal for int() with base 10: 'name'

# # *** So there is a point to remember 
# #     we just only can convert a number in string 
# #     we cannot convert type of value string to number ***


# print(int(c) + b)
# # >> 53
#       # *** and remember if string is like these 
#       #     '243', '23' 
#       #     then we can convert this number to a int and 
#       #     we can do the math 
# ------------------------

# 5 video content (Functions)

  # 1- Built in Functions 
  # 2- User defined Functions

  #   If we need to see what are the Built-in Functions;
  #       >>> dir(__builtins__)

# a = dir(__builtins__)
# print(a)

# and there is important Built-in Function
    # help() --> thats helps us to the see how to working 
    #            a built in function 

# print(help(pow)) 
# >> .. ... 
#   we can get a power using pow 
# print(pow(2, 4))
# >> 16
# ----------------------------------------

# 6 video content (Python Strings)

# # **1 How to use \ (forward slash) in strings
# print('nimal\'s')
# # >> nimal's

# print('it\'s')
# # >> it's

  # *** index numbers in Strings ------

# x = 'Eranda Prasad'
# print(x[4]) 
# # >> d

# print(x[2 : 6])
# # >> anda 

# print(x[2 : ])
# # >> anda Prasad

# print(x[ : 8])
# # >> Eranda P

# ------------ .replace()

# a = 'nayana'

# z = a.replace('a' , 'i')
# print(z)
# # >> niyini

# b = 'Kamal Nishantha'

# c = b.replace('Nishantha' , 'Perera')
# print(c)
# # >> Kamal Perera

# ------------ .split() and .join()

# name = 'Thisara Perera'

# z = name.split(' ')
# print(z)
# # >> ['Thisara', 'Perera']


# y = ' and '.join(z)
# print(y)
# # >> Thisara and Perera

# ------------------------------------

# 7 video content (Comparison Operators in Python)

    # ==     equal
    # !=     not equal
    # >      greater than 
    # <      less than 
    # >=     greater than or equal
    # <=     less than or equal 


# --------------------------------------

# 8 video content (If Else Statement)

# if --->> executes when it is True

# if True:
#     print('hello')
# # >> hello

# a = 10 

# if a == 10 :
#   print('The number is 10')
# else :
#   print('The number is not 10')

# # >> The number is 10

# ------------------------------------



# 9 video content (Python Collections)
    # list []----------

  # ** In python we use collection to store different types 
  #    of data values

  # ** There are index numbers for the List[];
  # ** We can change the elements inside the list
  # ** we can add the elements to the list - insert(), append() 
  # ** we can remove the elements inside the list - remove(), pop()
  # ** we can see the length of list using len()
  # ** we can clear the elements inside the list clear()
  # and we can delete the list del


# x = ['name', 234, 23.34, False]

# print(x[3])
# # >> False 

# # chnage elements inside the list 

# x[1] = 'age'
# print(x)
# # >> ['name', 'age', 23.34, False]

# # the length of the list 

# print(len(x))
# # >> 4


# # Insert elements to the list - with index number and insert

# x.insert(0 , 'Eranda')
# print(x)
# # >> ['Eranda', 'name', 'age', 23.34, False]


# # Add a element end of the list 

# x.append('this is append')
# print(x)
# # >> ['Eranda', 'name', 'age', 23.34, False, 'this is append']


# # remove a element inside the list 

# x.remove('Eranda')
# print(x)
# # >> ['name', 'age', 23.34, False, 'this is append']


# # remove the last element from the list 

# x.pop()
# print(x)
# # >> ['name', 'age', 23.34, False]


# # delte a list 

# # del x 
# # print(x)
# # >> NameError: name 'x' is not defined


# # clear elements from the list 
# x.clear()
# print(x)
# # >> []



# -------- more features in the list -------------

# a = [12, 0, 4, -4] 
# a.sort(reverse= True)
# print(a)
# # >> [12, 4, 0, -4]

# a.sort(reverse= False)
# print(a)
# # >> [-4, 0, 4, 12]


# ----------

# more other details about the list 

# a, b, c, d = [1, 2, 3, 4]
# print(a)
# >> 1

# a, b, *c = [1, 2, 3, 4, 5, 6]
# print(b)
# # >> 2

# print(c)
# # >> [3, 4, 5, 6]

# -------------- summary of this lesson -----

  # .len()     ------    show the length 
  # .insert()   ------    add a element inside the list 
  # .append()  ------    add a element end of the list 
  # .remove()  ------    remove a element from the list 
  # .pop()     ------    remove the last element from the list
  # .cler      ------    clear elements from the list 
  #  del       ------    delete the list 
  # .sort(reversed = True) desending order 10-0
  # .sort(reversed = False) asending order 0-10

# x.len()
# x.insert(3, 'kamal')
# x.append(19)
# x.remove('Kamal')
# x.pop()
# x.clear()
# del x



# a = [12, 12 ,32 ]
# print(a)

# a.insert(12, (12, 23,23))
# print(a)
# # >> [12, 12, 32, (12, 23, 23)]

# ----------------------------------------------

# 10 video content (Tuple)

# **** There is very important to remember  
#         ** we can't change elements inside the tuple


  # len() 
  # del 

# x = (1, 2, 3, 4)

# print(len(x))
# # >> 4

# # x.clear()
# # print(x)
# # >> AttributeError: 'tuple' object has no attribute 'clear'

# del x 
# print(x)
# # >> NameError: name 'x' is not defined

# so we can only see the length and can only do the delete 


# ----- list speed vs tuple speed -----

# import timeit

# list_time = timeit.timeit(stmt = "[1, 2, 3, 4]")
# tuple_time = timeit.timeit(stmt = "(1, 2, 3, 4)")

# print(list_time * 100)
# print(tuple_time * 100)

# >> 
# 8.348769998701755
# 1.6570700012380257

# # *** so from this result we can understand that tuple much 
# #     is faster more than list

# ------------------- The first 10 lessons are over ------------










