list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# -1-
for num in list_data:
    print(num*2)

# -2-
#for data in embedded_lists:
#    print(data)

# -3-
for data in embedded_lists:
    print(data)
    for individual in data:
        print(individual)

# -4-
for key in dict_data.keys():
    print(key)

# -5-
for val in dict_data.values():
    print(val)

# -6-
for val in dict_data.values():
    for val2 in val.values():
        print(val2)

# -7-
for val in dict_data.values():
    print(val['money'])

# -8-
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found 3")
    else:
        print("greater than 3")