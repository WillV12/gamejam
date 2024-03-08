respect_level=50
import random
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
            respect -= 25
            print(f"Respect Level: {respect}")
            break
        else:
            tries +=1
    print("Maybe unplugging those wires was not the way to bring the server back. ")

wire_unplug_challenge(respect_level)