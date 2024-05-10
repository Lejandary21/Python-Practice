score = 0
QUESTION_FORMAT = "{}\nA. {} B. {} C. {} D. {}"
# Intro
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
print("this quiz is about capital cities of the world.")
#Question 1
play = "yes"
while play == "yes":
    question = "What is the capital of New Zealand?"
    a = "Wellington"
    b = "New York"
    c = "London"
    d = "Rio De Janeiro"
    answer  = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    score += 5
    if answer.lower() == a or answer.lower() == "a":
        print("Correct! It is indeed Wellington")
    elif answer == "":
        print("Oh naur...")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print("That wasn't an option")
    else: 
        print("Sorry! That's incorrect. :(")
        print("The correct answer is Wellington! Better luck next time.")
    #Question 2
    answer =input("What's Australia's capital city?").upper()
    if answer == "CaNbErRa".upper():
        print("Correct! It is indeed Canberra. Good job!")
        score += 5
    elif answer == "":
        print("Did your keyboard break?")
    else: 
        print("Sorry! That's incorrect. :(")
        print("The correct answer is Canberra! Better luck next time.")
    #Question 3
    answer =input("What's Japan's capital city?").upper()
    if answer == "ToKyO".upper():
        print("Correct! It is indeed Tokyo!")
        score +=5
    elif answer == "":
        print("Did something short-circuit?")
    else:
        print("Sorry! That's incorrect. :(")
        print("The correct answer is Tokyo! Better luck next time.")
    # Ending
    print("Good job {}! Thank you so much for answering my quiz! Your final score {}.".format(name, score)) 
    play = input("Do you want to play again?").lower()
    try:
        tries = input("How many attempts do you want at each question? 1-3")
        tries = int(tries)
    except:
        print("That's not a number unfortunately. Maybe type 1, 2 or 3.")

print("Oh okay! Goodbye then! ^_^")