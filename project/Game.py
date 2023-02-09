from pickletools import uint1
import random

uw = 0                          #uw = user wins
cw = 0                          #cw = computer wins

options = ["stone", "paper", "scissors"]

while True:
    ui = input("Type Stone/Paper/Scissors or Q to quit: ")                #ui = user input
    if ui == "q":
        break

    if ui not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    cp = options [random_number]
    print("Computer picked", cp + ".")           #cp = computer pick

    if ui == "stone" and cp == "scissors" :            
        print ("You won!!")
        uw += 1

    elif ui == "paper" and cp == "stone" :
        print ("You won!!")
        uw += 1

    elif ui == "scissors" and cp == "paper" :
        print ("You won!!")
        uw += 1

    else:
        print ("You lost!!")
        cw += 1

print ("You won", uw, "times.")
print ("The computer won", cw, "times.") 
print ("Goodbye!!")