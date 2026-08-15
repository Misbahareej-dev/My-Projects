print("==============================")
print("          QUIZ GAME")
print("==============================")

score = 0

questions = [
    ("What does CPU stand for?", "A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Utility", "D. Control Processing User", "a"),
    ("Which language is commonly used for web page structure?", "A. Python", "B. HTML", "C. SQL", "D. Java", "b"),
    ("What does RAM stand for?", "A. Read Access Memory", "B. Random Access Memory", "C. Run Access Machine", "D. Random Application Memory", "b"),
    ("Which language is used to style web pages?", "A. HTML", "B. Python", "C. CSS", "D. SQL", "c"),
    ("Which device is used to connect a computer to a network?", "A. Router", "B. Keyboard", "C. Monitor", "D. Printer", "a"),
    ("Which language is mainly used for database queries?", "A. HTML", "B. CSS", "C. SQL", "D. Python", "c"),
    ("What does AI stand for?", "A. Automated Internet", "B. Artificial Intelligence", "C. Advanced Information", "D. Artificial Internet", "b"),
    ("Which one is an operating system?", "A. Windows", "B. Python", "C. Google", "D. HTML", "a"),
    ("Which data structure follows FIFO?", "A. Stack", "B. Queue", "C. Tree", "D. Graph", "b"),
    ("Which symbol is used for a comment in Python?", "A. //", "B. /* */", "C. #", "D. --", "c")
]

for number, question in enumerate(questions, 1):
    print("\n" + str(number) + ". " + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    answer = input("Enter your answer: ").lower()

    if answer == question[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n==============================")
print("       QUIZ COMPLETED")
print("==============================")
print("Your Score:", score, "/ 10")

if score >= 8:
    print("Excellent!")
elif score >= 5:
    print("Good Job!")
else:
    print("Keep Practicing!")

print("==============================")