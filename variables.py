respect_level= 50
# below 30, above 70, danger zone
# server

def bitcoin():
    pass
def chatgpt():
    pass
def roblox():
    pass
def food():
    pass
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
        respect += 25
        print (f"Respect Level: {respect}")
    elif choice == 2:
        print("Good job for trying to do the right thing, but snitching? That's mean.")
        respect -= 10
        print(f"Respect Level: {respect}")
    elif choice == 3:
        print("An employee should try to resolve issues and not ignore them. ")
        respect -= 25
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
        respect += 25
        print(f"Respect Level: {respect}")
    elif choice == 2:
        print("Good job for trying to do the right thing, but snitching? That's mean.")
        respect -= 10
        print(f"Respect Level: {respect}")
    elif choice == 3:
        print("An employee should try to resolve issues and not make it even worse. ")
        respect -= 25
        print(f"Respect Level: {respect}")
    else:
        choice = int(input("Option: "))
def upgrade(respect):
    pass
def admin_access():
    pass
def office_ransack():
    pass
def lanschool():
    pass

office_issues = [admin_access(), office_ransack(), lanschool()]
room_251_issues = [chatgpt(), roblox(), food(), bitcoin()]
server_issues = [spill_coffee(respect_level), burn(respect_level), upgrade(respect_level) ]

def software_unaccess():
    pass
def slow_wifi():
    pass
def servers_down():
    pass
def online_textbook():
    pass
def wiped_hard_drives():
    pass

issues = [software_unaccess(), slow_wifi(), servers_down(), online_textbook(), wiped_hard_drives()]

# def server():
#         choices = [1,2,3]
#         print("You have entered the server room."
#               "\n1. Check traffic"
#               "\n2. Unplug some wires"
#               "\n3. Look around")
#         choice = int(input("Option: "))
#         while choice not in choices and choice != 3:
#             print ("Make sure it is just the number of one of the options above.")
#             choice = int(input("Option: "))
#         if choice == 1:
#             print("Checking Traffic ....."
#                   "\nThere is no traffic at all. The servers are down."
#                   "\nMaybe look at something else.")
#
#         elif choice == 2:
#             pass
#         elif choice ==3:
#             pass
#         #print ("You have found the flashdrive with the server's upgrade.")
#         #inventory.apppend("Server Update Flashdrive")