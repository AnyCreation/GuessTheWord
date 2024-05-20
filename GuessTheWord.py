import random
import Vocabulary # type: ignore
import Join

SCORE = "C:/Users/User/Pictures/StupiedGame/Score.txt" # Fail txt for User's Score 

def Game(Number, Steps): # Game |X| 

    print("(_-_-_-_-_-_-_-_-The Game Begins-_-_-_-_-_-_-_-_)\n") # Start Game
    print(f"Number is: 1 - {Number} | Give Step: {Steps} \n") # Give Info About The Game

    Is_win = False # False - Lose, True - Win
    while True: #Game
        
        try: # Try - Get Number From User |X|
            Choice = float(input(f"(~~~ {Steps} chances left: ~~~) \n--Guess The Number-- \n~~choice: ")) # Gets A Number From The User
            
        except ValueError: # Expect - If The User Entered A Non-Number |X|
            # ↓↓ The Vocabulary difficultly Has A List Of Messages To Display If The User Doesn't Enter A Number ↓↓
            GER = len(Vocabulary.Is_Not_A_Number)
            print(f"{Vocabulary.Is_Not_A_Number[random.randint(0, GER - 1)]} \n") # Gave Random Messages If The User Doesn't Enter A Number
            continue

        if Choice > Number or Choice < 1: # If The Number Is Greater Than (Max_Number) Or Less Than 1
            print("!!Read The Rules!!\n") 
            continue
        elif Choice > Num: # If The Number Provided By The User Is Greater Than The Correct Number.
            print("The Number is... ↓↓Less↓↓ \n")
        elif Choice < Num: # If The Number Provided By The User Is Less Than The Correct Number.
            print("The Number is... ↑↑Greater↑↑ \n")
        else: # f The Number Provided By The User Is Correct Number.
            Is_win = True

        Steps -= 1

        if Steps == 0 or Is_win:
            return [Is_win, Steps]

User_Name, User_Password = Join.Join() # Join User

# (|--- ↓↓ Mods For The Game ↓↓ ----------------------------------|)
# Settings For Each Game Difficulty - [Max_Number, Max_Steps]
difficulty = {
    "easy": [10, 12],
    "medium": [20, 10],
    "hard": [30, 8],
    "delta": [10, 30],
    "fortuna": [10, 1]
    }

print("-- Try yourself --")
Choice_difficulty = input("Easy? medium? Hard? Delta? Fortuna?: ").lower() # Select Game Difficulty

Max_Number = difficulty[Choice_difficulty][0] # The Maximum Possible Number For Random /Can See In  "difficulty"/
Max_Steps = difficulty[Choice_difficulty][1] # The Maximum Steps Number For User /Can See In  "difficulty"/

if Choice_difficulty in ["easy", "medium", "hard", "fortuna"]: # If Difficulty Is Not "delta"
    Num = random.randint(1, difficulty[Choice_difficulty][0])
elif Choice_difficulty == "delta": # If Difficulty Is "delta", Float-Number, Float-Game 
    Num = round(random.uniform(1, difficulty[Choice_difficulty][0]), 3)
# (|--- ↑↑ Mods For The Game ↑↑ ----------------------------------|)



# (|--- ↓↓ Join And Create New User ↓↓ ----------------------------------|)
with open(SCORE, "r") as file: # Read txt Fail
    lines = file.readlines()

user_found = False
for Check_Info in range(0, len(lines)):
    if ':' not in lines[Check_Info]:
        continue
    User_Info, User_Score = lines[Check_Info].split(":")

    if User_Info.split("-")[0] == User_Name and User_Info.split("-")[1] == User_Password:
        point, wins, losses = User_Score.split(",")
        point = float(point.split("=")[1].strip())
        wins = float(wins.split("=")[1].strip())
        losses = float(losses.split("=")[1].strip())
        print(f"Welcome \"{User_Name}\" \n")
        user_found = True
        break

if User_Name == "" and User_Password == "": 
    User_Name = "NoUser"
    point = 0.0
    wins = 0.0
    losses = 0.0
    user_found = True

if not user_found: 
    with open(SCORE, 'a', encoding='utf-8') as file:
        if lines: 
            file.write("\n")
        file.write(f'\n{User_Name}-{User_Password}: point = 0.0, wins = 0.0, losses = 0.0')
    with open(SCORE, "r") as file:
        lines = file.readlines()
    point = 0.0
    wins = 0.0
    losses = 0.0
# (|--- ↑↑ Join And Create New User ↑↑ ----------------------------------|)

User_Win = Game(Max_Number, Max_Steps) # Start Game |X|, Return If Win Or Not

# (|--- ↓↓ Print Result (Win Or Lost) - Changes The Score ↓↓ ----------------------------------|)
if User_Win[0]: #Print If User Wins
    print("\n-- ((YOU WON!!)) --")
    print(f"Steps Left: {User_Win[1]}\n")
    
    if Choice_difficulty in ["easy", "medium", "hard"]:
        wins += Max_Number / 5 # If User Wins In difficulty --> Easy: 2, Medium: 4, Hard: 6
        
    elif Choice_difficulty == "delta":
        wins += 8 # If User Wins In difficulty "delta" --> User get 8
        
    else:
        wins += 10 # If User Wins In difficulty "Fortuna" --> User gets 10
else: #Print If User Lose
    print("\n~~ ((You lost!!)) ~~")
    print(f"The Number Was... {Num}\n")
    
    if Choice_difficulty in ["easy", "medium", "hard"]:
        losses += Max_Number / 10 # If User Loses In difficulty --> Easy: 1, Medium: 2, Hard: 3 
        
    elif Choice_difficulty == "delta":
        losses += 4 # If User Wins In difficulty "delta" --> User gets 4
        
    else:
        losses += 1 # If User Wins In difficulty "Fortuna" --> User gets 1
#(|--- ↑↑ Print Result (Win Or Lost) - Changes The Score ↑↑ ----------------------------------|)

point = ((wins * 3) - losses) / 2 # Finale Score

# (|--- ↓↓ We Are Looking For A Line With The Required User_Name To Save The Information ↓↓ ----------------------------------|)
for i, line in enumerate(lines):
    if User_Name in line:
        # If The Line Contains User_Name, Replace It With A New Line With Updated Data
        lines[i] = f"{User_Name}-{User_Password}: point = {point}, wins = {wins}, losses = {losses}"
        break

with open(SCORE, 'w', encoding='utf-8') as file:
    file.writelines(lines)
# (|--- ↑↑ We Are Looking For A Line With The Required User_Name To Save The Information ↑↑ ----------------------------------|)


#Score Menu
print("-----------------|")
print(f"--- {User_Name} ---")
print(f"Point = {point}")
print(f"Wins = {wins}")
print(f"Losses = {losses}")
print("-----------------|")
