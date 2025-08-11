print("""   _                      
                  | |                     
  __ _ _ __  _ __ | | __ _ _   _ ___  ___ 
 / _` | '_ \| '_ \| |/ _` | | | / __|/ _ \
| (_| | |_) | |_) | | (_| | |_| \__ \  __/
 \__,_| .__/| .__/|_|\__,_|\__,_|___/\___|
      | |   | |                           
      |_|   |_|                     """)

print("welcome to treasure island")
print("your mission is to find the treasure.")
choice1 =input("you are at the crossroad, where do " \
"you want to go.Type'left' or 'right': "). lower()

if choice1 == "left" :
    choice2 =input("You have come to  lake. There isan island in the middle of the lake."
                   "Type 'wait' if you want to wait for a boat.Type 'swim' to swim across: "). lower()
    if choice2 == "wait":
       choice3 = input("you have arrived at the island. " \
                       "there is a house with three doors: one red one yellow and one blue. " \
                       "which door do you choose? ").lower()
       if choice3 == "red":
          print("its a room full of fire.Game over")
       elif choice3 == "yellow":
          print("you found the treasure.You win!")
       elif choice3 == "blue":
          print("you entered a room full of beasts.Game over.")
       else :
          print("you have being attacked . Game over.")
    else:
      print("You got attacked by a trout. Game over.")       
else:   
   print("you fell into a hole. Game over.")

