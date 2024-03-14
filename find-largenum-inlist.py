def find_large_num(numbers):
  if not numbers:
    return None

  largest = numbers[0]

  for num in numbers[:]:
    if num > largest:
      largest = num

  return largest


number_list = [200, 5, 2, 65, 100, 33, 44]
# number_list = []


largerst_number = find_large_num(number_list)
print("The largest number is: ", largerst_number)



