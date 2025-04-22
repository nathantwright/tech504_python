dict_1 = {"ab": 12,
            "bc": 33,
            "cd": 1}
dict_2 = {"ab": 33,
            "bc": 1,
            "cd": 12}
dict_3 = {"ab": 2,
            "bc": 12,
            "cd": 33}
dict_list = [dict_1, dict_2, dict_3]

total = 0
for dictionary in dict_list:
    total += dictionary["ab"]

print(sum(dict_1.values()))
print(total)