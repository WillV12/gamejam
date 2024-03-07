# respect_level= 50
# def spill_coffee(respect):
#     print (f"Respect level: {respect}:")
#     print("You walk into the server room and realize someone spilled a cup of hot coffee all over the server racks."
#           "")
#
# spill_coffee(respect_level)
import variables
import random
# def wire_unplug_challenge():
#     tries = 0
#     wires = [1,2,3,4,5,6]
#     print ("Let's unplug some wires!"
#            "\nChoose wire number to unplug (1-6)")
#     while tries < 5:
#         wire = int(input("Wire: "))
#         if wire not in wires:
#             print ("Not one of the wires.")
#             wire = input("Wire: ")
#         wires.remove(wire)
#
#         tries +=1

options = [1, 2, 3]
print("You have entered the server room."
      "\n1. Check traffic"
      "\n2. Unplug some wires"
      "\n3. Look around")
choice = int(input("Option: "))
while choice not in options :
    print("Make sure it is just the number of one of the options above.")
    choice = int(input("Option: "))
while choice not in options or choice != 3:
    if choice == 1:
        print("Checking Traffic ....."
              "\nThere is no traffic at all. The servers are down."
              "\nMaybe look at something else.")
        #options.remove(choice)
        choice = int(input("Option: "))
    elif choice == 2:
        #wire_unplug_challenge()
        print("")
        choice = int(input("Option: "))
    elif choice == 3:
        print ("OhNo! You might have found the issue.")
        spill_coffee()
        burn()
        upgrade()
    else:
        choice = int(input("Option: "))
