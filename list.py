# list comprehension
fruits=["apple","banana","kiwi","grapes"]
new_fruits=[ fruits  for fruits in fruits if "a" in fruits]
print(new_fruits)

# copy a list
new_fruits=fruits.copy()
print(new_fruits)

new_fruits =fruits+new_fruits
print(new_fruits)

# nested list
fruits.insert(2,["kiwi","banana"])
print(fruits)
print(fruits[2][0])