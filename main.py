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
SHORT_OPINIONS = ["a", "b", "c", "d"]
ANSWERS = [0,0,1]
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
    answer  = input(QUESTION_FORMAT.format(QUESTIONS[0], OPTIONS[0][0],
                                           OPTIONS[0][1], OPTIONS[0][2], OPTIONS[0][3])).lower()
    score += 5
    if answer == OPTIONS[0][ANSWERS[0]] or answer == SHORT_OPINIONS[ANSWERS[0]]:
        print("Correct! It is indeed Wellington")
        print(random.choice(GOOD_COMMENTS))
    elif answer == "":
        print("Oh naur...")
    elif answer in  SHORT_OPINIONS or answer in OPTIONS[0]:
        print("That's incorrect!")
        print(random.choice(BAD_COMMENTS))
    else: 
        print("That wasn't an option...")
# Ending
    print("Good job {}! Thank you so much for answering my quiz! Your final score {}.".format(name, score)) 
    play = input("Do you want to play again?").lower()
    print("Oh okay! Goodbye then! ^_^")