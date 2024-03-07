# below 30, above 70, danger zone
# server
import random
respect_level = 0
status_level = 0


def rand_choice(lower, upper, chance):
    success = True
    randit = random.randint(lower, upper)
    if randit <= chance:
        success = False
    return success


def error_check(user, num_questions):

    error = user.isnumeric() is False or not 1 <= int(user) <= num_questions
    return error


def bitcoin(respect, status): # Dillion
    pass
def chatgpt(respect, status): # Dillion
    pass
def roblox(respect, status): # Dillion
    pass
def food(respect, status): # Dillion
    pass
def spill_coffee(respect, status): # Carol
    pass
def burn(respect, status): # Carol
    pass
def upgrade(respect, status): # Carol
    pass
def admin_access(respect, status): # Will
    print("")
def stuxnet(inventory, status):
    print("You were walking from the parking lot to your office, when you notice a USB drive on the ground..."
          "\nWhat do you do?\n")
    print("1.pick up the drive\n2.leave it alone\n3.Give it to campus police\n")
    choice = input("What will you do?\n")
    while error_check(choice, 3):
        print("Incorrect response\n1-3")
        choice = input("What will you do?\n")

    if choice == "1":
        inventory.append("USB")
        print("USB added to inventory!!!\n")
    elif choice == "2":
        print("You leave it alone and head to your office\n")
    elif choice == "3":
        print("The campus police thanked you!\nYour employers noticed this...\n+10 status")
        status += 10
    return status

def office_ransack(respect, status): # Will
    pass
def lanschool(respect, status): # Will
    pass

office = [admin_access(respect_level,status_level), office_ransack(respect_level,status_level), lanschool(respect_level,status_level)]
room_251 = [chatgpt(respect_level,status_level), roblox(respect_level,status_level), food(respect_level,status_level), bitcoin(respect_level,status_level)]
server = [spill_coffee(respect_level,status_level), burn(respect_level,status_level), upgrade(respect_level,status_level)]

def software_unaccess(respect, status):
    pass

    pass
def slow_wifi(respect, status):
    pass
def servers_down(respect, status):
    pass
def online_textbook(respect, status):
    pass
def wiped_hard_drives(respect, status):
    pass

issues = [software_unaccess(respect_level,status_level), slow_wifi(respect_level, status_level),
          servers_down(respect_level,status_level), online_textbook(respect_level,status_level),
          wiped_hard_drives(respect_level, status_level)]