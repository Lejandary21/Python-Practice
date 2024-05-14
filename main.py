import random
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D. {}"
GOOD_COMMENTS =  ["Nice one!", "Good job!", "Brilliant!"]
BAD_COMMENTS = ["Womp womp...", "Good try but try again!", ]
QUESTIONS = ["What is the capital of New Zealand?",
                "What's Australia's capital city? ",
                    "What's Japan's capital city?"]
OPTIONS = [["Wellington", "New York", "London", "Rio De Janeiro"],
           ["Canberra", "Sydney", "Melbourne", "Brisbane"],
           ["Kyoto", "Tokyo", "Osaka", "Kawasaki"]]

# Intro
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
print("this quiz is about capital cities of the world.")
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-3")
        tries = int(tries)
        break
    except:
        print("That's not a number unfortunately. Maybe type 1, 2 or 3.")
play = "yes"
while play == "yes":
    score = 0

    #Question 1
    question = "What is the capital of New Zealand?"
    a = "Wellington"
    b = "New York"
    c = "London"
    d = "Rio De Janeiro"
    answer  = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    score += 5
    if answer.lower() == a or answer.lower() == "a":
        print("Correct! It is indeed Wellington")
        print(random.choice(GOOD_COMMENTS))
    elif answer == "":
        print("Oh naur...")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print("That wasn't an option")
    else: 
        print("The correct answer is Wellington! Better luck next time.")
        print(random.choice(BAD_COMMENTS))
#Question 2
    answer =input("What's Australia's capital city?").upper()
    if answer == "CaNbErRa".upper():
        print("Correct! It is indeed Canberra. Good job!")
        print(random.choice(GOOD_COMMENTS))
        score += 5
    elif answer == "":
        print("Did your keyboard break?")
    else: 
        print(random.choice(BAD_COMMENTS))
        print("The correct answer is Canberra! Better luck next time.")
#Question 3
    answer =input("What's Japan's capital city?").upper()
    if answer == "ToKyO".upper():
        print("Correct! It is indeed Tokyo!")
        print(random.choice(GOOD_COMMENTS))
        score +=5
    elif answer == "":
        print("Did something short-circuit?")
    else:
        print(random.choice(BAD_COMMENTS))
        print("The correct answer is Tokyo! Better luck next time.")
# Ending
    print("Good job {}! Thank you so much for answering my quiz! Your final score {}.".format(name, score)) 
    play = input("Do you want to play again?").lower()
    print("Oh okay! Goodbye then! ^_^")