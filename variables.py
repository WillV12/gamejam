# status below 30, respect above 70, danger zone
# server
import random
import ascii
import Room_251
respect_level = 50
status_level = 50
inventory = []


def rand_choice(lower, upper, chance):
    success = True
    randit = random.randint(lower, upper)
    if randit <= chance:
        success = False
    return success


def bitcoin(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "bitcoin")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:", inventory)
    status = new_statuses[0]
    respect = new_statuses[1]
    new_statuses.clear()


def chatgpt(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "chat gpt")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:", inventory)
    status = new_statuses[0]
    respect = new_statuses[1]
    new_statuses.clear()


def roblox(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "roblox")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:", inventory)
    status = new_statuses[0]
    respect = new_statuses[1]
    new_statuses.clear()


def food(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "food")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:", inventory)
    status = new_statuses[0]
    respect = new_statuses[1]
    new_statuses.clear()
def spill_coffee(respect, status): # Carol
    pass
def burn(respect, status): # Carol
    pass
def upgrade(respect, status): # Carol
    pass
def admin_access(respect, status): # Will
    print("")


def office_ransack(respect, status): # Will
    pass
def lanschool(respect, status): # Will
    pass

office = [admin_access(respect_level,status_level), office_ransack(respect_level,status_level), lanschool(respect_level,status_level)]
room_251 = [chatgpt(respect_level,status_level), roblox(respect_level,status_level), food(respect_level,status_level), bitcoin(respect_level,status_level)]
server = [spill_coffee(respect_level,status_level), burn(respect_level,status_level), upgrade(respect_level,status_level)]

def software_unaccess(respect, status):
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






