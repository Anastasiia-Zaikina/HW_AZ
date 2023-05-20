import re

camel_case = ["FirstItem", "FriendsList", "MyTuple"]

result_list = []

for element in camel_case:
    result_list.append(re.sub(r'(?<!^)(?=[A-Z])', '_', element).lower())

print(result_list)
