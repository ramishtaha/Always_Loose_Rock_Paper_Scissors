print("Welcome to Always loose Rock Paper Scissors")

inp = input("Enter Rock, Paper or Scissors. To Yield enter 'yield'\n")
while inp != "yield":
    if inp == "Rock":
        print("Paper, You Loose.")
    elif inp == "Paper":
        print("Scissors, You Loose.")
    elif inp == "Scissors":
        print("Rock, You Loose.")
    else:
        print("Please enter correct Values")
    inp = input("Enter Rock, Paper or Scissors. To Yield enter 'yield'\n")

print("I told you will never win in this game.")
