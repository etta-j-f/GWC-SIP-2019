import json

f = open("answers.json", "r")
x = json.load(f)
f.close()
# print(x)
# print(type(x))

sum_ages = 0
for i in x:
    print(i["what is your name? "])
    # if
#     sum_ages += age
#     lstage.append(age)
# avg = sum_ages / len(x)
# print(avg)
# print(lst_ages)
