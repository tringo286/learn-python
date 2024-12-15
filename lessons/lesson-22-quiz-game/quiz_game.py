# Quiz Game

questions = (
    "How many bones are in the human body?",
    "What is the largest organ in the human body?",
    "How many chromosomes do humans have?",
    "What is the function of the heart?",
    "What is the process of photosynthesis?"
)

options = (
    ("A: 206", "B: 205", "C: 210", "D: 200"),
    ("A: Heart", "B: Skin", "C: Brain", "D: Liver"),
    ("A: 46", "B: 23", "C: 44", "D: 48"),
    ("A: Pump blood", "B: Store oxygen", "C: Break down food", "D: Produce hormones"),
    ("A: Plants make food from sunlight", "B: Plants absorb water", "C: Animals breathe oxygen", "D: Plants release carbon dioxide")
)


answers = ("A", "B", "A", "A", "A")
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print(f'{answers[question_num]}')
    question_num += 1

print('------------------')
print('      RESULTS     ')
print('------------------')

print('answers: ', end='')
for answer in answers:
    print(answer,end=' ')
print()

print('guesses: ', end='')
for guess in guesses:
    print(guess,end=' ')
print()

score = (score / len(questions) * 100) 
print(f'Your score is: {score}%')