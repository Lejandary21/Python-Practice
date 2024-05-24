guesses = []
BIGGEST_COUNTRIES_ANSWERS = ["russia", "canada", "china", "us", "brazil", "australia", "india", "argentina"]

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

# Check if answer already exists in list. Used for checking