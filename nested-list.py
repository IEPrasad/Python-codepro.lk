numbers = [1, 2, 3, 4, 6]
# ^^ this is a list 
# print(numbers[1])
# >> 2


nested_list = [1, 2, ['Nimal', "kamal", 50], 20]
# ^^ and this is a nested list 

    # Let's do some practice with nested list 


# so how we can access this nested elements

print(nested_list[2][1])
  # >> kamal

# how to change the value inside the nested list 

# nested_list[2][0] = 100
# print(nested_list)
  # >> [1, 2, [100, 'kamal', 50], 20]

print(nested_list[len(nested_list)-2][2])
# >> kamal, 50 

print(nested_list[len(nested_list)-2][ : 2])
# >> Nimal, Kamal

print(nested_list[len(nested_list)-2][ : : 2])
#  >> ['Nimal', 'Kamal']

