questions=("capital of india?",
           "how many bones are there in human body?",
           "how many planets are there in solar system?",
           "which animal cant fly?",
           "total elements in periodic table?")
options=(("A. DELHI", "B. KOLKATA", "C. JAIPUR", "D. JAIPUR"),
          ("A. 306", "B. 209", "C. 206", "D. 207"),
          ("A. 7", "B. 9", "C. 10", "D. 8"), 
          ("A. EAGLE", "B. OSTRICH", "C. CROW", "D. SPARROW"),
          ("A. 116", "B. 118", "C. 117", "D. 120"))

answers=("A", "C", "C", "B", "B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("-------------------------")
print("           RESULTS          ")
print("-------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score= int(score/ len(questions)*100)
print(f"your total score is: {score}%")