import random
pc_guess = random.choice(["Rock" , "Paper" ,"Scissors"])
player_guess = input("Make a guess : ").capitalize()
wine = {"Rock" : "Paper" , "Paper" : "Scissors" , "Scissors" : "Rock"}
if player_guess not in wine.values() : print("-----Write Correctly-----")
elif pc_guess == player_guess: print("-----Equal-----")
elif wine[pc_guess] == player_guess : print(f"Pc guess : {pc_guess}\n-----You Wine!!!-----") 
else: print(f"Pc guess : {pc_guess}\n-----You lose-----")