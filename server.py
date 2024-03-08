import random

def spill_coffee(respect):
    options = [1, 2, 3]
    print("There is some coffee spilled all over the servers floor. Choose what you want to do:"
          "\n1. Clean it up"
          "\n2. Pull up video footage and snitch"
          "\n3. Leave it the way it is")
    choice = int(input("Option: "))
    while choice not in options:
        print("Make sure it is just the number of one of the options above.")
        choice = int(input("Option: "))
    if choice == 1:
        print("That is really kind. Good Job!")
        respect[0] += 25
        print (f"Respect Level: {respect}")
    elif choice == 2:
        print("Good job for trying to do the right thing, but snitching? That's mean.")
        respect[0] -= 10
        print(f"Respect Level: {respect}")
    elif choice == 3:
        print("An employee should try to resolve issues and not ignore them. ")
        respect[0] -= 25
        print(f"Respect Level: {respect}")
    else:
        choice = int(input("Option: "))

def burn(respect):
    options = [1, 2, 3]
    print("Apparently, someone also burned one of the power outlets here in the server. What do you do?"
          "\n1. Call the maintenance dude"
          "\n2. Pull up video footage and snitch"
          "\n3. Burn another one")
    choice = int(input("Option: "))
    while choice not in options:
        print("Make sure it is just the number of one of the options above.")
        choice = int(input("Option: "))
    if choice == 1:
        print("That is really kind. Good Job!")
        respect[0] += 25
        print(f"Respect Level: {respect}")
    elif choice == 2:
        print("Good job for trying to do the right thing, but snitching? That's mean.")
        respect[0] -= 10
        print(f"Respect Level: {respect}")
    elif choice == 3:
        print("An employee should try to resolve issues and not make it even worse. ")
        respect[0] -= 25
        print(f"Respect Level: {respect}")
    else:
        choice = int(input("Option: "))

def wire_unplug_challenge(respect):
    tries = 0
    wires = [1,2,3,4,5,6]
    print ("Let's unplug some wires!"
           "\nChoose wire number to unplug (1-6)")
    while tries < 2:
        print("Available Wires")
        for i in wires:
            print(f"Wire:{i}")
        print("")
        explode = random.randint(1, 6)
        wire = int(input("Wire: "))
        if wire not in wires:
            print ("Not one of the wires.")
            wire = input("Wire: ")
        wires.remove(wire)
        if wire == explode:
            print ("OH NO! You just exploded the server!")
            respect[0] -= 25
            print(f"Respect Level: {respect}")
            break
        else:
            tries +=1
    print("Maybe unplugging those wires was not the way to bring the server back. ")

def server(respect_level):
    options = [1, 2, 3]
    print("You have entered the server room."
          "\n1. Check traffic"
          "\n2. Unplug some wires"
          "\n3. Look around")
    choice = int(input("Option: "))
    while True:
        while choice not in options :
            print("Make sure it is just the number of one of the options above.")
            choice = int(input("Option: "))
        if choice in options and choice == 1:
            print("Checking Traffic ....."
                    "\nThere is no traffic at all. The servers are down."
                    "\nMaybe look at something else.")
            choice = int(input("Option: "))
        elif choice in options and choice == 2:
            wire_unplug_challenge(respect_level)
            print("")
            choice = int(input("Option: "))
        elif choice in options and choice == 3:
            print ("OhNo! You might have found the issue.")
            print("")
            spill_coffee(respect_level)
            print("")
            burn(respect_level)
            print("")
            #upgrade(respect_level)
            break
        else:
            choice = int(input("Option: "))


