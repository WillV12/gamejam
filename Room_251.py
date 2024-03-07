# Dillon Kondylas
# 03/07/2024
# This simulates the room 251 portion of the game
import ascii
import random

inventory = []
# run this command every time clint goes to 251, command statuses =s[ the new status and r]espect after changes
def room_251(status, respect, event):
    print("You are in room 251 now.")
    print("Status:", status)
    print("Respect:", respect)
    if 33 < status < 66:
        ascii.mccuen("neutral")
    elif -1 < status < 34:
        ascii.mccuen("angry")
    elif 67 < status < 101:
        ascii.mccuen("happy")
    if event == "bitcoin":

        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been mining bitcoin in class!\n What do you do?")
            print("""
            1. send students to office
            2. ignore it
            3. wipe all the computers
            4. attack McCuen!""")
            choice = input("\n")
        if choice == "1":
            print("\nYou sent the student to the office...\n(status +5) (respect -5)")
            statuses = [status+5, respect-5]
        elif choice == "2":
            print("\nYou ignored it!!!\n(status -20) (respect +15)")
            statuses = [status-15, respect+15]
        elif choice == "3":
            print("\nYou wiped the computers!!!\n(status -15) (respect -20)")
            statuses = [status-15, respect-20]
        elif choice == "4":
            ascii.mccuen("angry")
            print("You did not win...\nWhat were you thinking...")
            print("(status -25)\n(respect - 25)")
            statuses = [status-25, respect-25]
    elif event == "chat gpt":
        print("The Students have been using ChatGPT to cheat in class!\n What do you do?")
        print("""
        1. tell them to scroll down
        2. ignore it
        3. block the openAI website
        4. attack McCuen!""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been using ChatGPT to cheat in class!\n What do you do?")
            print("""
                    1. tell them to scroll down
                    2. ignore it
                    3. block the openAI website
                    4. attack McCuen!""")
            choice = input("\n")
        if choice == "1":
            print("\nYou told them to scroll down...\n(status -10) (respect +10)")
            statuses = [status-10, respect+10]
        elif choice == "2":
            print("\nYou ignored it!!!\n(status -20) (respect +15)")
            statuses = [status-20, respect+15]
        elif choice == "3":
            print("\nYou blocked that website!!!\n(status +15) (respect -10)")
            statuses = [status+15, respect-10]
        elif choice == "4":
            ascii.mccuen("angry")
            print("He used the chewbacca defence...\nYou did not aquit fast enough...")
            print("(status -25)\n(respect - 25)")
            statuses = [status-25, respect-25]

    if "ceiling beam that almost hit nuno on the head..." not in inventory:
        if random.randint(1, 4) == 1:
            inventory.append("ceiling beam that almost hit nuno on the head...")
            print("You found a ceiling beam that almost hit nuno on the head!!!\nceiling beam that almost hit nuno on the head... added to inventory.")

    print("You leave 251...\n\n")
    return statuses


event = input("What is the event?\n").lower()
new_statuses = room_251(50, 50, event)
print("Status:", new_statuses[0])
print("Respect:", new_statuses[1])
print("Inventory:", inventory)
