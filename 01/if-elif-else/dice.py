from random import randint

sides = input("sides?")
sides = int(sides)

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")

player1_dice_roll = randint(1, sides)
player2_dice_roll = randint(1, sides)
a=player1_dice_roll
b=player2_dice_roll

print(name1 + " rolled: " + str(player1_dice_roll))
print(name2 + " rolled: " + str(player2_dice_roll))

if(a==b):
   print "Draw"
elif(a>b):
   print ( name1 + " wins!")
else: 
   print ( name2 + " wins!")
