def count_duplicates(list):
  for item in list:
    key_1 = list.count(item)
    list_1[item] = key_1

  min_value = min(list_1.values())


  for key, value in list_1.items():
    if value == max_value:
      print(f"{key}:{value}")
    elif value == min_value:
      print(f"{key}:{value}")

