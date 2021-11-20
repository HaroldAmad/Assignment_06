import random
score = 0
questions = {}

for i in range(10):
    first_number = random.randint(0,99)
    second_number = random.randint(0,99)
    operation = ('+')
    question = str(first_number)+" "+operation+" "+str(second_number)
    answer = str(eval(question))
    question+='= '

    questions.update({question:answer})

for q in questions.keys():
    user_answer = input(q)
    if questions.get(q)==user_answer:
        score+=1
        print("Correct!")
    else:
        print("Incorerct!")
    
print('You got '+str(score)+'/10. ')

