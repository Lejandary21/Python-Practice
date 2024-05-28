import random
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D. {}"
GOOD_COMMENTS =  ["Nice one!", "Good job!", "Brilliant!"]
BAD_COMMENTS = ["Womp womp...", "Good try but try again!", ]
QUESTIONS = ["What is the capital of New Zealand?",
                "What's Australia's capital city? ",
                    "What's Japan's capital city?",
                        "What's the capital of China?"]
OPTIONS = [["Wellington", "New York", "London", "Rio De Janeiro"],
           ["Canberra", "Sydney", "Melbourne", "Brisbane"],
           ["Kyoto", "Tokyo", "Osaka", "Kawasaki"],
           ["Nanjing", "Shanghai", "Guangzhou", "Beijing"]]
SHORT_OPINIONS = ["a", "b", "c", "d"]
ANSWERS = [0,0,1,3]

play = "yes"
# Intro
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
print("this quiz is about capital cities of the world.")
#Attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-3")
        tries = int(tries)
        break
    except:     
        print("That's not a number unfortunately. Maybe type 1, 2 or 3.")
#Starting the quiz
while play == "yes":
    score = 0
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
        #Questions
            answer  = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                            OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPINIONS[ANSWERS[i]]:
                print("Correct! It is indeed Wellington")
                print(random.choice(GOOD_COMMENTS))
                score += 5
                break
            elif answer == "":
                print("Oh naur...")
            elif answer in  SHORT_OPINIONS or answer in OPTIONS[i]:
                print("That's incorrect!")
                print(random.choice(BAD_COMMENTS))
                question_attempts -=  1
            else: 
                print("That wasn't an option...")
            
# Ending
    print("Good job {}! Thank you so much for answering my quiz! Your final score {}.".format(name, score)) 
    play = input("Do you want to play again?").lower()
    print("Oh okay! Goodbye then! ^_^")