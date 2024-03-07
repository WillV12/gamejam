# Dillon Kondylas
# 03/07/2024
# This simulates the room 251 portion of the game
import ascii
import random
import variables

inventory = []
# run this command every time clint goes to 251, command returns the new status and respect values
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
    elif event == "roblox":
        print("The Students have been playing Roblox in class!\n What do you do?")
        print("""
        1. tell them to swap to A on the switch
        2. Wipe all the computers
        3. block Roblox
        4. Reply with AI generated response""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("The Students have been playing Roblox in class!\n What do you do?")
            print("""
                    1. tell them to swap to A on the switch
                    2. Wipe all the computers
                    3. block Roblox
                    4. Reply with AI generated response""")
            choice = input("\n")
        if choice == "1":
            print("\nYou told them to be on the A switch...\n(status -10) (respect +0)")
            statuses = [status-10, respect+0]
        elif choice == "2":
            print("\nYou wiped all the computers!!!\n(status -15) (respect -20)")
            statuses = [status-15, respect-20]
        elif choice == "3":
            print("\nYou blocked that website!!!\n(status +15) (respect -10)")
            if "\"concerning\" letter from student" not in inventory:
                if variables.rand_choice(0, 100, 60):
                    inventory.append("\"concerning\" letter from student")
                    print("You recieved a...concerning...letter from a student after you blocked roblox!!!")
            statuses = [status+15, respect-10]
        elif choice == "4":
            print("""Dear Mr. McCuen,

While Roblox engagement in class could offer both educational benefits and 
distractions, finding a balance that aligns with our objectives is key.

Best regards,
[Your Name]\n""")
            print("(status -25)\n(respect +20)")
            statuses = [status-10, respect+5]
    elif event == "food":
        print("The Students have been eating food in class!\n What do you do?")
        print("""
        1. eat all their food
        2. report them to wake tech
        3. report them to WECIB
        4. Don't do anything""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("The Students have been eating food in class!\n What do you do?")
            print("""
                    1. eat all their food
                    2. report them to WECIB
                    3. report them to Wake Tech
                    4. Don't do anything""")
            choice = input("\n")
        if choice == "1":
            print("\nYou ate all their food!!! WHYYYY!!!\n(status -15) (respect -25)")
            statuses = [status - 3, respect - 15]
        elif choice == "2":
            print("\nYou reported them to WECIB!!! \n(WECIB does not care, "
                  "\"That's Wake Tech's problem...\")\n(status +5) (respect -2)")
            statuses = [status + 5, respect - 2]
        elif choice == "3":
            print("\nYou reported them to Wake Tech!!!\n(Wake Tech banished them to the shadow realm)\n(status +10) (respect -10)")
            statuses = [status + 10, respect - 10]
        elif choice == "4":
            print("I'm not a narc!!!\n")
            print("(status -20)\n(respect +20)")
            statuses = [status - 10, respect + 5]
        if variables.rand_choice(0, 100, 50):
            inventory.append("napkins")
            print("you found napkins!")

    if "ceiling beam that almost hit nuno on the head..." not in inventory:
        if random.randint(1, 4) == 1:
            inventory.append("ceiling beam that almost hit nuno on the head...")
            print("\nYou found a ceiling beam that almost hit nuno on the head!!!\nceiling beam that almost hit nuno on the head... added to inventory.\n")

    print("You leave 251...\n\n")
    return statuses

new_statuses = room_251(50, 50, event)
print("Status:", new_statuses[0])
print("Respect:", new_statuses[1])
print("Inventory:", inventory)
status = new_statuses[0]
respect = new_statuses[1]
new_statuses.clear()
