import random
questions = {}
score = 0

for i in range(10):
    first_number = random.randint(0,99)
    second_number = random.randint(0,99)
    operator = ['+']
    questions = str(first_number) +''+ str(operator) +''+ str(second_number)
    answer = eval(questions)
    questions+=': '

    questions.update ({questions:str(answer)})

for q in questions.keys():
    user_answer = input (q)
    if questions.get(q) == user_answer:
