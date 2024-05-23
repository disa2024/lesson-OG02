list = [1,1,1,2,2,1,8,5,4,6,5,9,2,3,4,6,2,1,5,8,7,4,5,9,6,3,2,5,4,6,7,8,9,1,2,3,4,5,6,7,8]

list_1 = {}

def count_duplicates(list):
  for item in list:
    key_1 = list.count(item)
    list_1[item] = key_1

  max_value = max(list_1.values())
  min_value = min(list_1.values())

  for key, value in list_1.items():
    if value == max_value:
      print(f"{key}:{value}")
    elif value == min_value:
      print(f"{key}:{value}")

count_duplicates(list)