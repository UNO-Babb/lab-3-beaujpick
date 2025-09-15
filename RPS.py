#RPS.py
#Name: Beau Pick
#Date: 9-14-25
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0

wins = 0
ties = 0
losses = 0


print("Record: W/T/L", int(wins), int(ties), int(losses))

while True:
  choose = input("Enter your weapon (R for Rock, P for Paper, S for Scissors): ").upper()
  if choose not in ("R", "P", "S"):
      print ("Invalid, please choose R, P, or S.")
      continue

  output = random.choice (["R", "P", "S"])
  print(f"Computer chose: {output}")

  if choose == output:
      print("You Tied!")
      ties = ties + 1
  elif (choose == "R" and output == "S") or \
        (choose == "P" and output == "R") or \
        (choose == "S" and output == "P"):
      print("You Win!!")
      wins = wins + 1
  else:
      print ("You Lose!!")
      losses = losses + 1


  print("Record: W/T/L", int(wins), int(ties), int(losses))

 
  again = input ("Play Again? (Y/N): ").upper()
  if again == "N":
      break






  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats



