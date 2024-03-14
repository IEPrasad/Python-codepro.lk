def find_smallest_number(numbers):
  if not numbers:
    return None
  
  min_num = numbers[0]
  for num in numbers:
    if num < min_num:
      min_num = num
    
  return min_num


number_list = [45,23,23,45,1,445]

min_number = find_smallest_number(number_list)
print("The smallest number is: ", min_number)
