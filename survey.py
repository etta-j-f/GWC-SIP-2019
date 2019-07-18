import json

def takesurvey(questions, answers):
    answer = {}
    for q in questions:
        answer[q] =  input(q)
    # print(answer)
    answers.append(answer)
    # print(answers)


a = []

q = ['what is your name? ', 'What is your nationality? ', 'How old are you? ', 'What is your favorite ice cream flavor? ',
'Do you play any sports? ', 'What about instruments? ' , 'What genre music do you like? ' , 'What color is your hair? ' , 'Is water wet? ']

for i in range(3):
    print("NEW SURVEY")
    takesurvey(q, a)
print(a)

f = open("answers.json" ,"w")
f.write(json.dumps(a))
f.close()
