from pathlib import Path
import os
import random
import json

with open("coutriesAndCapitals.json") as sheet:
    capitals = json.load(sheet)

# how many quizes you want
quiztestNumber = input('give me the Quiz test number please: ')
method = input("what method you want : text/json")

while method != "text" and method != "json":
    method = input("what method you want : text / json ")

directorypath = Path.home() / 'quizgame'
if not directorypath.exists():
    os.mkdir(directorypath)

if method == "text":
    for i in range(int(quiztestNumber)):
        test = f'{directorypath}\\quiz{i + 1}.txt'
        answer = f'{directorypath}\\answer{i + 1}.txt'
        quiztest = open(test, 'w')
        quizanswer = open(answer, 'w')
        quiztest.write(f'quiz number {i + 1}'.center(60))
        quiztest.write('\n\n')
        states = list(capitals.keys())
        random.shuffle(states)
        for j in range(len(states)):
            rightanswer = capitals[states[j]]
            wronganswers = list(capitals.values())
            del wronganswers[wronganswers.index(rightanswer)]
            possibleanswers = random.sample(wronganswers, 3)+[rightanswer]
            random.shuffle(possibleanswers)
            # fill in quiz test  file
            quiztest = open(test, 'a')
            quiztest.write(
                f'quiz{j+1} : what is the capital of {states[j]} ? '.center(60))
            quiztest.write('\n')
            for k in range(len(possibleanswers)):
                quiztest.write(f'{"ABCD"[k]}.{possibleanswers[k]}'.center(60))
                quiztest.write('\n')
            quiztest.write('\n')
            # write the right asnwer in quiz answer file
            quizanswer = open(answer, 'a')
            quizanswer.write('\n')
            quizanswer.write(
                f'quiz number {j+1} : {"ABCD"[possibleanswers.index(rightanswer)]}'.center(60))
            quizanswer.write('\n')
            quiztest.close()
            quizanswer.close()
elif method == "json":
    pass            

print(f"the quizes are made and saved in {directorypath}")
