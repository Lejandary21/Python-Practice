score = 0
# Intro
name = input("What's your name?")
print("Hello! Welcome to the quiz" ,name)
print("this quiz is about capital cities of the world.")
#Question 1
question = "What is the capital of New Zealand?"
a = "Wellington"
b = "New York"
c = "London"
d = "Rio De Janeiro"
answer  = input("{})\nA.{} B.{} C. {} D. {}".format(question, a, b, c, d)).lower()

score += 5
if answer.lower() == a or answer.lower() == "a":
    print("Correct! It is indeed Wellington")
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
print("Good job {}! Thank you so much for answering my quiz! Your final score {} out of 15".format(name, score)) 