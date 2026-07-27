"""
                               PROJECT NAME = CHOOSE YOUR OWN ADVENTURE 
"""
def game_lose():
    print("YOU LOSE THE Adventure")
    print("...............................................")
    print("...GAME OVER...")
    return

def game_win():
    print(name, "you collect all the gem successfully")
    print("YOU WON THE Adventure")
    print("...............................................")
    print("...GAME OVER...")
    return

name= input("Type your name: " )
print(f"Welcome {name} to the Adventure!")
adventure= input("Choose your Adventure.....for Jungle enter(Jungle) or for Road enter(Road) ").upper()

if(adventure== "JUNGLE"):
    print("Now, you enter in the jungle")
    choice= input("If you want to swim in river enter(SWIM) or If you want to run on ground enter(RUN): ").upper()

    if(choice== "SWIM"):
        print(name, "is swiming in river")
        print(name, "was eaten by a crocodile.")
        game_lose()

    elif(choice== "RUN"):
        print(name, "is running on ground")
        print(name, "enter in the cave")
        game_win()

    else:
        print("Invalid Choice")
        
elif(adventure== "ROAD"):
    print("Now, you are on the Highway")
    choice= input("If you want to run on highway enter(HIGHWAY) or If you want to sit in car enter(CAR): ").upper()

    if(choice== "HIGHWAY"):
        print(name, "is running on the Highway")
        print(name, "was hit by a car.")
        game_lose()

    elif(choice== "CAR"):
        print(name, "is sitting in the Car ")
        print(name, "enter in the Building")
        game_win()
    
    else:
        print("Invalid Choice")

else:
    print("Invalid Choice")



