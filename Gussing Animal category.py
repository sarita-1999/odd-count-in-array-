import random
class Game():
    user_name =''
    category =''
    animals = ''
    def __init__(self,user_name):
        print (" Welcome ", user_name, "! Lets begin the game.")
        self.user_name = user_name
        self.initialize_dict()
        self.play()
    def initialize_dict(self):
        self.animals = {'parrot': "I am a bird; I am green in color and have reddish beak",
            'peacock': "I am a bird. I am colorful and known as the national bird of India",
            'hen': "I am a domestic bird and give you eggs for omelette",
            'crocodile': "I am a reptile; I am brownish green in colour, big in size and live in water.",
            'snake': "I am a reptile. I make a hiss sound and can move without any legs",
            'lizard': "I am a reptile; I live in most houses and I can easily crawl on the walls",
            'bee': "I am an insect and I help with pollination and collect honey",
            'mosquito': "I am an insect and I drink blood and spread disease",
            'butterfly': "I am an insect and I have beautiful wings and I love nectar "}
    def play(self):
        print( "Guess who I am from the below hints ")
        animals=self.animals  # Initiating  local variable for animals 
        random_animal = random.choice(list(self.animals.keys()))  #Convert keys into 
        hints = self.animals.get(random_animal)
        print (hints)
        print ( "your guess : ")
        guess = input().lower().strip()
        #get input from user here
        #convert guess to all lowercase and remove any whitespaces from the beginning or end.
        if guess == random_animal:
            print("You are right!")
        else:
            print("Wrong guess!")
            print("Would you like to continue the game (Y/N)")
            if input().upper()=="Y":    # get user input and if "Y"
                self.play()
           # print("Would you like to continue the game (Y/N) ?")
           # if input().upper()=="Y":    # get user input and if "Y"
            #    self.play()
if __name__ == "__main__":
    print(" Welcome to animal guessing game. Please enter your name: ")
    user_name = input( )
#get user name and store it in the variable user_name. IT will be passed to the constructor of Game class
    Game= Game(user_name)




