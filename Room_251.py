# Dillon Kondylas
# 03/07/2024
# This simulates the room 251 portion of the game
import ascii
import random

# I just used these variables for testing
"""inventory = []
Status = [int(input("status"))]
Respect = [int(input("respect"))]
Event = input("event").lower()"""


# run this command every time clint goes to 251, command returns the new status and respect values in a list
# status and respect need to be between 0 and 100
# valid event inputs: "talk", "bitcoin", "roblox", "chat gpt", "food"

def room_251(status, respect, event):
    statuses = [status, respect]
    print("You are in room 251 now.")
    print("Status:", status)
    print("Respect:", respect)
    staring_competition = ""

    # status determines McCuen's joy to see you for talking...
    if 31 < status[0] < 70:
        if event == "talk":
            while True:
                ascii.mccuen("neutral")
                print("\nHi. I'm Mr.McCuen\n")
                print("1. \"Hey Russ can I talk to you for a moment?\"\n2. *blank stare*\n3. leave\n")
                choice1 = input("")
                if choice1 == "3":
                    print("\nSee ya Clint...\n")
                    break
                elif choice1 == "2" or choice1 == "1":
                    while True:
                        if choice1 == "1":
                            ascii.mccuen("neutral")
                            print("\nYeah sure, what's up?")
                        else:
                            ascii.mccuen("neutral")
                            print("Is there something you wanna talk about??")
                        print("\n1. Roblox\n2. Teams\n3. Wifi Cable\n4. Favorite student?!?")
                        if choice1 == "2":
                            print("5. *keep staring* \n6. back\n")
                            choice2 = input("")
                            if choice2 == "6":
                                break
                            elif choice2 == "5":
                                print("\nMan I'm getting kinda weirded out right now...\n")
                                x = 0
                                while x < 4:
                                    staring_competition_reactions = ["\nHey don't make me mad!",
                                                                     "\nYou're gonna regret this!", ""]
                                    print(staring_competition_reactions[x-1])
                                    staring_competition = ""
                                    while staring_competition != "1" and staring_competition != "2":
                                        print("\n1. *Keep Staring*\n2. Back\n")
                                        staring_competition = input("")
                                    if staring_competition == "2":
                                        break
                                    elif x == 2 and staring_competition == "1":
                                        ascii.mccuen("instinct")
                                        print("I always win staring contests...\n(status-20) (respect -25)\n")
                                        statuses = [status[0] - 20, respect[0] - 25]
                                        break
                                    x += 1
                        elif choice1 == "1":
                            print("5. back")
                            choice2 = input("")
                        if staring_competition == "1":
                            break
                        if choice2 == "1":
                            print("""
                            \"Oh yeah that's a video game that the back row plays a lot, I have no clue 
                            what in the world it's about because everytime I look at Lanschool it's just a bunch of 
                            colors and annoying sounds... but that back row has a lot of fun doing whatever it is that 
                            happens on Roblox... Oh yeah also I let them play it if they finished all their work.\"\n""")
                            input("\nPress Enter to continue...\n")
                        elif choice2 == "2":
                            print("""
                            \"Don't even get me started on Teams! That app is genuinely the worst app in 
                            the whole history of apps! It crashes half the time and doesn't work, the few times that it
                            does work, It's incredibly slow! Messanger Pidgeons would be better than Teams any day of 
                            the week. PERIOD.\"\n""")
                            input("\nPress Enter to continue...\n")
                        elif choice2 == "3":
                            print("\n\"HAHAAH... that's the dumbest and best thing i've heard all day...\"\n")
                            input("\nPress Enter to continue...\n")
                        elif choice2 == "4":
                            print("""
                            \"Whaaaaat?! A favorite student?! No wayyyy... I don't have a favorite
                            student! That's crazy...\"
                            \"But Carol, Dillon, and Will are pretty awesome...\"\n""")
                            input("\nPress Enter to continue...\n")
                        elif choice2 == "5":
                            break
                    if staring_competition == "1":
                        break
        else:
            ascii.mccuen("neutral")
    elif -1 < status[0] < 31:
        if event == "talk":
            while True:
                ascii.mccuen("angry")
                print("1. \"Hey Russ can I talk to you for a moment?\"\n2. *blank stare*\n3. leave\n")
                choice1 = input("")
                def dismemberment():
                    ascii.mccuen("instinct")
                    body_parts = ["your own severed left arm", "also your right arm", "Goodness! both of your legs",
                                  "Somehow it's your own spinal cord???"]
                    counter = 0
                    while counter < len(body_parts)+1:
                        if counter >= len(body_parts):
                            if "Golden Coding Duck" not in inventory:
                                rand_num = random.randint(0, 100)
                                print(rand_num)
                                if rand_num == 42:
                                    print("Mr.McCuen has actually severed all that he is able to from your body."
                                      "\nIn a fit of rage he throws his prized Golden Coding Duck at you...")
                                    print("Added to inventory:", "Golden Coding Duck")
                                    inventory.append("Golden Coding Duck")
                                    counter = len(body_parts) + 1
                                else:
                                    print("Why (and how) do you persist?! His anger has already consumed most of "
                                          "thine body")
                                    counter = len(body_parts) + 1
                            else:
                                print("You've taken everything from this man's anger, go annoy someone else please")
                                counter = len(body_parts) + 1
                        elif body_parts[counter] not in inventory:
                            print("\nTake this, you may need it on your journey...")
                            print(f"Enraged Mr.McCuen hands you: {body_parts[counter]}\n{body_parts[counter]} "
                                  f"added to inventory.")
                            inventory.append(body_parts[counter])
                            counter = len(body_parts) + 1
                        else:
                            counter += 1
                    input("\nPress enter to continue...")
                if choice1 == "2":
                    dismemberment()
                elif choice1 == "3":
                    print("\nSo glad he's gone...\n")
                    break
                elif choice1 == "1":
                    while True:
                        if choice1 == "1":
                            ascii.mccuen("angry")
                            print("\nWhat.")
                        print("\n1. Roblox\n2. Teams\n3. Wifi Cable\n4. Favorite student?!?\n5. back")
                        choice2 = input("")
                        if choice2 == "1":
                            print("""
                            \"Why do YOU care?! >:(\"\n""")
                        elif choice2 == "2":
                            print("""
                            \"Teams is the only thing I hate more than you.\"\n""")
                        elif choice2 == "3":
                            print("\n\"...\"\n")
                        elif choice2 == "4":
                            print("""
                            \"My favorite student is anyone but you, and you aren't even a student\"
                            \"But Carol, Dillon, and Will are pretty awesome...\"\n""")
                        elif choice2 == "5":
                            break
                        input("Press enter to continue...")
        else:
            ascii.mccuen("angry")
    elif 69 < status[0] < 101:
        if event == "talk":
            while True:
                ascii.mccuen("happy")
                print("Hey, I'm Russ!")
                print("1. \"Hey Russ can I talk to you for a moment?\"\n2. *blank stare*\n3. leave\n")
                choice1 = input("")
                if choice1 == "2":
                    print("Oh Boy I love staring contests!!!")
                    while True:
                        print("\nHe just keeps staring...\n")
                        print("1. *keep staring*\n2. give up\n")
                        choice2 = input("")
                        if choice2 == "2":
                            print("Haha I beat you!")
                            input("\nPress enter to continue...")
                            break
                elif choice1 == "3":
                    print("\nBye Clint!!! I miss you already!!!\n")
                    break
                elif choice1 == "1":
                    while True:
                        if choice1 == "1":
                            ascii.mccuen("happy")
                            print("\nCLINT!!! I'm so happy to talk to you")
                        print("\n1. Roblox\n2. Teams\n3. Wifi Cable\n4. Favorite student?!?\n5. back")
                        choice2 = input("")
                        if choice2 == "1":
                            print("""
                            \"Oh boy Roblox is just the best game ever isn't it? there's so much to do
                            and an endless amount of creativity and joy to be had!!!\"\n""")
                        elif choice2 == "2":
                            print("""
                            \"The best part about Teams is being able to talk to you\"\n""")
                        elif choice2 == "3":
                            print("\n\"HAHAHAHAHAHHAHHAHAHHAHAHAHAHAHAHAHHAHAHAHAHHAHAHA\n(deep inhale)\nHAHAHAHAHAHHAHAH"
                                  "HAHAHAH\nWOW CLINT THAT IS SO FUNNY!!!\"\n")
                        elif choice2 == "4":
                            print("""
                            \"My favorite student is you!!! and you aren't even a student\"
                            \"But Carol, Dillon, and Will are pretty awesome...Easily top 5...\"\n""")
                        elif choice2 == "5":
                            break
                        input("Press enter to continue...")
        else:
            ascii.mccuen("happy")

    if event == "bitcoin":
        print("The Students have been mining bitcoin in class!\n What do you do?")
        print("""
                    1. send students to office
                    2. ignore it
                    3. wipe all the computers
                    4. attack McCuen!""")
        choice = input("\n")
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
            statuses = [status[0]+5, respect[0]-5]
        elif choice == "2":
            print("\nYou ignored it!!!\n(status -20) (respect +15)")
            statuses = [status[0]-15, respect[0]+15]
        elif choice == "3":
            print("\nYou wiped the computers!!!\n(status -15) (respect -20)")
            statuses = [status[0]-15, respect[0]-20]
        elif choice == "4":
            ascii.mccuen("instinct")
            print("You did not win...\nWhat were you thinking...")
            print("(status -25)\n(respect - 25)")
            statuses = [status[0]-25, respect[0]-25]
        input("\npress enter to continue...\n")
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
            statuses = [status[0]-10, respect[0]+10]
        elif choice == "2":
            print("\nYou ignored it!!!\n(status -20) (respect +15)")
            statuses = [status[0]-20, respect[0]+15]
        elif choice == "3":
            print("\nYou blocked that website!!!\n(status +15) (respect -10)")
            statuses = [status[0]+15, respect[0]-10]
        elif choice == "4":
            ascii.mccuen("instinct")
            print("He used the chewbacca defence...\nYou were forced to aquit...")
            print("(status -25)\n(respect - 25)")
            statuses = [status[0]-25, respect[0]-25]
        input("\npress enter to continue...\n")
    elif event == "roblox":
        print("The Students have been playing Roblox in class!\n What do you do?")
        print("""
        1. tell them to swap to A on the switch
        2. Wipe all the computers
        3. block Roblox
        4. Reply with AI generated response""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been playing Roblox in class!\n What do you do?")
            print("""
                    1. tell them to swap to A on the switch
                    2. Wipe all the computers
                    3. block Roblox
                    4. Reply with AI generated response""")
            choice = input("\n")
        if choice == "1":
            print("\nYou told them to be on the A switch...\n(status -10) (respect +0)")
            statuses = [status[0]-10, respect[0]+0]
        elif choice == "2":
            print("\nYou wiped all the computers!!!\n(status -15) (respect -20)")
            statuses = [status[0]-15, respect[0]-20]
        elif choice == "3":
            print("\nYou blocked that website!!!\n(status +15) (respect -10)")
            if "\"concerning\" letter from student" not in inventory:
                if random.randint(0, 100) < 60:
                    input("\npress enter to continue...\n")
                    inventory.append("\"concerning\" letter from student")
                    print("You recieved a...concerning...letter from a student after you blocked roblox!!!")
            statuses = [status[0]+15, respect[0]-10]
        elif choice == "4":
            print("""Dear Russel McCuen,

While Roblox engagement in class could offer both educational benefits and 
distractions, finding a balance that aligns with our objectives is key.

Best regards,
[Your Name]\n""")
            print("(status -25)\n(respect +20)")
            statuses = [status[0]-10, respect[0]+5]
        input("\npress enter to continue...\n")
    elif event == "food":
        print("The Students have been eating food in class!\n What do you do?")
        print("""
        1. eat all their food
        2. report them to wake tech
        3. report them to WECIB
        4. Don't do anything""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been eating food in class!\n What do you do?")
            print("""
                    1. eat all their food
                    2. report them to WECIB
                    3. report them to Wake Tech
                    4. Don't do anything""")
            choice = input("\n")
        if choice == "1":
            print("\nYou ate all their food!!! WHYYYY!!!\n(status -15) (respect -25)")
            statuses = [status[0] - 3, respect[0] - 15]
        elif choice == "3":
            print("\nYou reported them to WECIB!!! \n(WECIB does not care, "
                  "\"That's Wake Tech's problem...\")\n(status +5) (respect -2)")
            statuses = [status[0] + 5, respect[0] - 2]
        elif choice == "2":
            print("\nYou reported them to Wake Tech!!!\n(Wake Tech banished them to the shadow realm)\n(status +10) (respect -10)")
            statuses = [status[0] + 10, respect[0] - 10]
        elif choice == "4":
            print("I'm not a narc!!!\n")
            print("(status -20)\n(respect +20)")
            statuses = [status[0] - 10, respect[0] + 5]
        input("\npress enter to continue...\n")
        if random.randint(0, 100) < 50:
            inventory.append("napkins")
            print("you found napkins!")
            input("\npress enter to continue...\n")
    if event != "talk":
        if "ceiling beam that almost hit nuno on the head..." not in inventory:
            if random.randint(1, 4) == 1:
                inventory.append("ceiling beam that almost hit nuno on the head...")
                print("\nYou found a ceiling beam that almost hit nuno on the head!!!\nceiling beam that almost hit nuno on the head... added to inventory.\n")
                input("\npress enter to continue...\n")

    print("You leave 251...\n\n")
    return statuses


#This command take the major issue as input like: Students cant access software/online books
# returns "bitcoin", "roblox", "food", "chat gpt"
def check_computers(major_issue, issue_list):
    # simulate forgetting username and password
    forget = random.choice(["nothing", "username", "password", "both"])
    if forget == "nothing":
        print("You flawlessly logged in without forgetting your username or password")
        pass
    elif forget == "username":
        print("You forgot your Username when trying to sign in to the computer... ")
        usernames = ["CMathews", "ExoticButters1337", "ILoveTeams", "admin", "username", "password", "Mr.Cisco"]
        while True:
            print("here are your guesses:\n")
            for x in range(len(usernames)):
                print(f" - {usernames[x-1]}")
            guess = input("\n(type the full username, not just it's number on the list)\n")
            while guess not in usernames:
                print("\nPlease enter one of Clint's guesses!")
                guess = input("\n(type the full username, not just it's number on the list)\n")
            if guess == random.choice(usernames):
                print("Good Job! you guessed your username!")
                break
            else:
                print("sorry that was not the right one...")
                usernames.remove(guess)
    elif forget == "password":
        print("You forgot your Password when trying to sign in to the computer... ")
        password = ["ILoveTeresa", "ScrollDown42", "ILoveJimMatlock", "admin", "username", "password", "lil Cisco"]
        while True:
            print("here are your guesses:\n")
            for x in range(len(password)):
                print(f" - {password[x - 1]}")
            guess = input("\n(type the full password, not just it's number on the list)\n")
            while guess not in password:
                print("\nPlease enter one of Clint's guesses!")
                guess = input("\n(type the full password, not just it's number on the list)\n")
            if guess == random.choice(password):
                print("Good Job! you guessed your password!")
                break
            else:
                print("sorry that was not the right one...")
                password.remove(guess)
    elif forget == "both":
        correctly_guessed_both_checker = [False, False]
        print("You forgot your Username AND Password when trying to sign in to the computer?!?!\nWHY DON'T YOU "
              "WRITE THIS STUFF DOWN?!?!? ")
        password = ["ILoveTeresa", "ScrollDown42", "ILoveJimMatlock", "admin", "username", "password", "lil Cisco"]
        usernames = ["CMathews", "ExoticButters1337", "ILoveTeams", "admin", "username", "password", "Mr.Cisco"]
        guess1 = ''
        guess2 = ''
        while True:
            print("here are your guesses:\n")
            if not correctly_guessed_both_checker[0]:
                print("\nUSERNAMES:")
                for x in range(len(usernames)):
                    print(f" - {usernames[x - 1]}")
            else:
                print("\nCORRECT USERNAME")
                print(" -", guess1)
            if not correctly_guessed_both_checker[1]:
                print("\nPASSWORDS:")
                for x in range(len(password)):
                    print(f" - {password[x - 1]}")
            else:
                print("\nCORRECT PASSWORD:")
                print(" -", guess2)
            if not correctly_guessed_both_checker[0]:
                guess1 = input("\n(type the full username, not just it's number on the list)\nUsername: ")
                while guess1 not in usernames:
                    print("\nPlease enter one of Clint's guesses!")
                    guess1 = input("\n(type the full username, not just it's number on the list)\nUsername: ")
                if guess1 == random.choice(usernames):
                    print("Good Job! you guessed your username!")
                    correctly_guessed_both_checker[0] = True
                else:
                    print("sorry that was not the right username...")
                    usernames.remove(guess1)
            if not correctly_guessed_both_checker[1]:
                guess2 = input("\n(type the full password, not just it's number on the list)\nPassword: ")
                while guess2 not in password:
                    print("\nPlease enter one of Clint's guesses!")
                    guess2 = input("\n(type the full password, not just it's number on the list)\nPassword: ")
                if guess2 == random.choice(password):
                    print("Good Job! you guessed your password!")
                    correctly_guessed_both_checker[1] = True
                else:
                    print("sorry that was not the right password...")
                    password.remove(guess2)
            if correctly_guessed_both_checker == [True, True]:
                print("\nCongratulations! You just guessed your username and password! ")
                print("Username:", guess1)
                print("Password:", guess2)
                print("NOW WRITE IT DOWN SOMEWHERE SO YOU WONT FORGET AGAIN!!!\n(Wake Tech will probably force you to "
                      "get a new username and password by the next time you log in...")
                inventory.append("sticky note with username and password")
                print("Added to inventory: sticky note with username and password.")
                break
    if major_issue == "can\'t access software":
        randomly_selected_minor_issue = random.choice(issue_list)
        if randomly_selected_minor_issue == "bitcoin":
            print("\nA few hours later...\n")
            print("You fixed the problem, but while you were at the computer, you\nnoticed the server fans operating "
                  "at over 100%, upon further inspection of\nthe computer you realize that students have been mining "
                  "bitcoin using\nwake tech property!\n")
            input("Press enter to continue...")
            return "bitcoin"
        elif randomly_selected_minor_issue == "roblox":
            print("\nA few hours later...\n")
            print("You fixed the problem, but while you were at the computer,\nyou noticed that many of the students had "
                  "an application\ncalled \"Roblox\" installed on their computers.\nFrom your knowlege it is a video game...\n"
                  "INSTALLED ON WAKE TECH PROPERTY?!?!\n")
            input("Press enter to continue...")
            return "roblox"
        elif randomly_selected_minor_issue == "food":
            print("\nA few hours later...\n")
            print("You fixed the problem, but while you were at the computer, you noticed\ncrumbs, grease, sprinkles, and "
                  "nearly every other kind\nof food residue imaginable baked into the keyboard,\nmouse, monitor, and even"
                  "somehow the motherboard...\n")
            input("Press enter to continue...")
            return "food"
        elif randomly_selected_minor_issue == "chat gpt":
            print("\nA few hours later...\n")
            print("You fixed the problem, but while you were at the computer, you\nnoticed most of the bandwidth on the "
                  "network being used for ChatGPT,\ntypically I would not care but this is an AI model\npossibly being used"
                  " to cheat\nI need to do something... or do I?\n")
            input("Press enter to continue...")
            return "chat gpt"
    elif major_issue == "can\'t access online textbook":
        randomly_selected_minor_issue = random.choice(issue_list)
        if randomly_selected_minor_issue == "bitcoin":
            print("\nA few hours later...\n")
            print("You were calling customer service all day, but you finally got\nthe students their textbooks. However,"
                  " Cutomer service commented\non how loud the servers were.\nI checked and the server fans were "
                  "operating at over 100%, upon\nfurther inspection of the computer you realize that students have been"
                  " mining\nbitcoin using wake tech property!\n")
            input("Press enter to continue...")
            return "bitcoin"
        elif randomly_selected_minor_issue == "roblox":
            print("\nA few hours later...\n")
            print("You were calling customer service all day, but you finally got\nthe students their textbooks. However,"
                  " Cutomer\nservice commented on how much traffic there was to\nRoblox.com. I checked and the many of "
                  "the students had\nan application called \"Roblox\" installed on their computers. From your\nknowlege "
                  "it is a video game...\nINSTALLED ON WAKE TECH PROPERTY?!?!\n")
            input("Press enter to continue...")
            return "roblox"
        elif randomly_selected_minor_issue == "food":
            print("\nA few hours later...\n")
            print("You were calling customer service all day, but you finally\ngot the students their textbooks. However,"
                  " Cutomer service commented\non how delicious the computers looked. I checked and there were crumbs, grease,"
                  " sprinkles,\nand nearly every other kind of food residue imaginable baked into the\nkeyboard, mouse,"
                  " monitor, and even somehow the motherboard...\n")
            input("Press enter to continue...")
            return "food"
        elif randomly_selected_minor_issue == "chat gpt":
            print("\nA few hours later...\n")
            print("You were calling customer service all day, but you finally got the\nstudents their textbooks. However,"
                  " Cutomer service commented on how much traffic\nthere was to OpenAI. I checked and most of the bandwidth on the "
                  "network being used for ChatGPT,\ntypically I would not care but this is an AI model possibly being used"
                  " to cheat\nI need to do something... or do I?\n")
            input("Press enter to continue...")
            return "chat gpt"
    elif major_issue == "none":
        randomly_selected_minor_issue = random.choice(issue_list)
        if random.randint(1, 100) < 33 or randomly_selected_minor_issue == "food":
            print(
                "\nYou did not catch anything while monitoring the computers...\n")
            input("Press enter to continue...")
        elif randomly_selected_minor_issue == "bitcoin":
            print(
                "\nSoon after logging onto the computer to monitor the computers, You caught\n"
                "many users pushing their computers with cost heavy Bitcoin software!!!\n")
            input("Press enter to continue...")
            return "bitcoin"
        elif randomly_selected_minor_issue == "roblox":
            print(
                "\nSoon after logging onto the computer to monitor the computers, you caught a bunch\n"
                "of students playing Roblox in the middle of a lecture!\n")
            input("Press enter to continue...")
            return "roblox"
        elif randomly_selected_minor_issue == "chat gpt":
            print(
                "\nSoon after logging onto the computer to monitor the computers, you caught\n"
                "many students using ChatGPT to cheat!")
            input("Press enter to continue...")
            return "chat gpt"
    elif major_issue == "slow wifi":
        print("FIX THE WIFI!!\nUnplug the router and plug it back in...")
        print("""
        \n===<|B|""")
        input("")
        print("""
                \n===<|=  B|""")
        input("")
        print("""
                \n===<|B|""")
        randomly_selected_minor_issue = random.choice(issue_list)
        if random.randint(1, 100) < 33 or randomly_selected_minor_issue == "food":
            pass
        elif randomly_selected_minor_issue == "bitcoin":
            print(
                "\nSoon after the internet went back up, You caught\n"
                "many users pushing their computers with cost heavy Bitcoin software!!!\n")
            input("Press enter to continue...")
            return "bitcoin"
        elif randomly_selected_minor_issue == "roblox":
            print(
                "\nSoon after the internet went back up, you caught a bunch\n"
                "of students playing Roblox in the middle of a lecture!\n")
            input("Press enter to continue...")
            return "roblox"
        elif randomly_selected_minor_issue == "chat gpt":
            print(
                "\nSoon after the server went back up, you caught\n"
                "many students using ChatGPT to cheat!")
            input("Press enter to continue...")
            return "chat gpt"


def office_mini_prompts(status, respect, event):
    statuses = [status, respect]
    print("You are in the office now.")
    print("Status:", status)
    print("Respect:", respect)

    if event == "admin access":
        print("The Students encountered admin access!\n What do you do?")
        print("""
                        1. send students to office
                        2. ignore it
                        3. give them admin access
                        4. fix it after school""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been mining bitcoin in class!\n What do you do?")
            print("""
                1. send students to office
                2. ignore it
                3. give them admin access
                4. fix it after school""")
            choice = input("\n")
        if choice == "1":
            print("\nYou sent the student to the office...\n(status -15) (respect -5)")
            statuses = [status[0] - 15, respect[0] - 5]
        elif choice == "2":
            print("\nYou ignored it!!!\n(status -20) (respect -15)")
            statuses = [status[0] - 20, respect[0] - 15]
        elif choice == "3":
            print("\nYou gave them admin access!!!\nThey are doing stuff they're not supposed to do\n(status -15) (respect +20)")
            statuses = [status[0] - 15, respect[0] + 20]
        elif choice == "4":
            print("You fixed the issue!")
            print("(status +10)\n(respect +15)")
            statuses = [status[0] - 25, respect[0] - 25]
        input("\npress enter to continue...\n")
    elif event == "students ransack office":
        print("The Students have Ransacked your office!!\n What do you do?")
        print("""
            1. tell them to scroll down
            2. cry
            3. Beat them up!
            4. Call the police""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("The Students have been using ChatGPT to cheat in class!\n What do you do?")
            print("""
            1. tell them to scroll down
            2. cry
            3. Beat them up!
            4. Call the police""")
            choice = input("\n")
        if choice == "1":
            print("\nYou told them to scroll down...\n(status -10) (respect -20)")
            statuses = [status[0] - 10, respect[0] - 20]
        elif choice == "2":
            print("\nYou Cried about it!!!\n(status -2) (respect -15)")
            statuses = [status[0] - 2, respect[0] - 15]
        elif choice == "3":
            print("\nYou tried to beat them up!!!\nYou lost!!!\n(status -25) (respect - 5)")
            statuses = [status[0] - 25, respect[0] - 5]
        elif choice == "4":
            print("you called the police!\nthe kids got arrested!")
            print("(status +15)\n(respect - 10)")
            statuses = [status[0] + 15, respect[0] - 10]
        input("\npress enter to continue...\n")
    elif event == "lan school issue":
        print("McCuen has an issue with lanschool\n What do you do?")
        print("""
            1. tell them to swap to A on the switch
            2. Wipe all the computers
            3. wipe McCuens computer
            4. fix the computer over the weekend""")
        choice = input("\n")
        while choice not in ["1", "2", "3", "4"]:
            print("Please make a choice...")
            print("McCuen has an issue with lanschool!\n What do you do?")
            print("""
            1. tell them to swap to A on the switch
            2. Wipe all the computers
            3. wipe McCuens computer
            4. fix the computer over the weekend""")
            choice = input("\n")
        if choice == "1":
            print("\nYou told them to be on the A switch...\n(status -2) (respect -5)")
            statuses = [status[0] - 2, respect[0] + 5]
        elif choice == "2":
            print("\nYou wiped all the computers!!!\n(status -10) (respect -20)")
            statuses = [status[0] - 10, respect[0] - 20]
        elif choice == "3":
            ascii.mccuen("instinct")
            print("\nYou wiped McCuen's computer!!!\n(status -25) (respect +20)")
            statuses = [status[0] - 25, respect[0] + 20]
        elif choice == "4":
            print("""\nYou fixed the computer over the weekend...\n""")
            print("(status +5)\n(respect +5)")
            statuses = [status[0] +5, respect[0] + 5]
        input("\npress enter to continue...\n")

# office_mini_prompts(Status, Respect, Event)
'''new_statuses = room_251(status, respect, Event)
print("Status:", new_statuses[0])
print("Respect:", new_statuses[1])
print("Inventory:")
if len(inventory) == 0:
    print("empty...")
else:
    for item in range(len(inventory)):
        print(" -", inventory[item-1])
status = new_statuses[0]
respect = new_statuses[1]
new_statuses.clear()

check_computers()'''
