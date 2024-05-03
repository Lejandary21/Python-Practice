score = 0
# Intro
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
print("this quiz is about capital cities of the world.")
#Question 1
answer =input("What's New Zealand's capital city?")
if answer == "Wellington" :
    print("Correct! It is indeed Wellington")
    score += 5
elif answer == "":
    print("Cat got your tongue?")
else: 
    print("Sorry! That's incorrect. :(")
    print("The correct answer is Wellington! Better luck next time.")
#Question 2
answer =input("What's Australia's capital city?")
if answer == "Canberra" :
    print("Correct! It is indeed Canberra. Good job!")
    score += 5
elif answer == "":
    print("Did your keyboard break?")
else: 
    print("Sorry! That's incorrect. :(")
    print("The correct answer is Canberra! Better luck next time.")
#Question 3
answer =input("What's Japan's capital city?")
if answer == "Tokyo" :
    print("Correct! It is indeed Tokyo!")
    score +=5
elif answer == "":
    print("Did something short-circuit?")
else:
    print("Sorry! That's incorrect. :(")
    print("The correct answer is Tokyo! Better luck next time.")
# Ending
print("Thank you for taking the quiz!")
print("Your final score is" ,score)