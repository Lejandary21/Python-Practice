guesses = []
BIGGEST_COUNTRIES_ANSWERS = ["russia", "canada", "china", "us", "brazil", "australia", "india", "argentina", "Kazakhstan", "Algeria"]

# ---FUNCTIONS---

#welcomes the users and introduces the quiz 
def intro():
    #Ask the user's name
    name = input("What's your name?")

#Greet the user and introduce the quiz
    print("Hello! Welcome to the quiz,", name)
    print("This quiz is about the ten largest countries in the world.")

# Ask user for the lives and confirm is valid
def getlives():
    while True:
        lives = input("How many chances do you want, friend?")
        try:
            #Checking if valid number
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

# Check if answer already exists in list. Used for checking both correct answers, and previous guesses.
def inList(answer,list):
    if answer in list:
        return True
    else:
        return False
    
#Main code

intro()
lives = getlives()
score = 0
# Begin the quiz 
while lives > 0:
    answer = input("Name one of the top 10 biggest countries in the world:\n").lower()
# Check if correct or wrong 
    if inList(answer, BIGGEST_COUNTRIES_ANSWERS):
        # Checks if already guessed or not
        if inList(answer, guesses):
            print("Sorry, but you've guessed that already!")
        else:
            print("That's correct!")
            score +=5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses))), score
    else:
        print("Wrong")
        lives -=1
        print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses))), score
              
# End the game
print("Game Over. Your final score was {}".format(score))
