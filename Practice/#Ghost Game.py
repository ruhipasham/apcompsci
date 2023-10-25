#Ghost Game

from random import randint

print("Welcome to \"Ghost Game\"")
print("A ghost is behind one of three doors ahead...\nChoose door that does not have a ghost?")
feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 3)
    door = input("Enter Door number 1, 2, or 3 : ")
    door_num = int(door)
    print("\nYou have chosen to enter room % s" % door_num)
    
    if door_num < 1 & door_num < 4:
        print("\nCannot find door % s Please retry!\n" % door)
    else:     
        if door_num == ghost_door:
            feeling_brave = False
            print("\n!!GHOST!! Run Away!\n Your scored: % s " % score)   
        else:
            print("\nNo Ghost! You can enter the room.")
            score = score + 1

    
    
