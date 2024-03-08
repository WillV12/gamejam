# status below 30, respect above 70, danger zone
# server
import random
import ascii
import Room_251
respect_level = [50]
status_level = [50]
inventory = []


def rand_choice(lower, upper, chance):
    success = True
    randit = random.randint(lower, upper)
    if randit <= chance:
        success = False
    return success


def bitcoin(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "bitcoin")
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])


def chatgpt(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "chat gpt")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()

def talk_mccuen():
    Room_251.room_251(status_level, respect_level, "talk")

def roblox(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "roblox")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()


def food(respect, status): # Dillion
    new_statuses = Room_251.room_251(status, respect, "food")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()


def spill_coffee(respect, status): # Carol
    pass


def burn(respect, status): # Carol
    pass


def upgrade(respect, status): # Carol
    pass


def admin_access(respect, status): # Will
    new_statuses = Room_251.office_mini_prompts(status, respect, "admin access")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()


def office_ransack(respect, status): # Will
    new_statuses = Room_251.office_mini_prompts(status, respect, "students ransack office")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()


def lanschool(respect, status): # Will
    new_statuses = Room_251.office_mini_prompts(status, respect, "lan school issue")
    print("Status:", new_statuses[0])
    print("Respect:", new_statuses[1])
    print("Inventory:")
    if len(inventory) == 0:
        print("empty...")
    else:
        for item in range(len(inventory)):
            print(" -", inventory[item - 1])
    status_level[0] = new_statuses[0]
    respect_level[0] = new_statuses[1]
    new_statuses.clear()


office = ["admin access", "office ransack", "lanschool"]
room_251 = ["chat gpt", "roblox", "food", "bitcoin"]
server = ["spill coffee", "burn", "upgrade"]


def software_unaccess(respect, status):
    minor_issue = Room_251.check_computers("can\'t access software", room_251)
    if minor_issue == "chat gpt":
        room_251.remove("chat gpt")
        chatgpt(respect, status)
    elif minor_issue == "roblox":
        room_251.remove("roblox")
        roblox(respect, status)
    elif minor_issue == "food":
        room_251.remove("food")
        food(respect, status)
    elif minor_issue == "bitcoin":
        room_251.remove("bitcoin")
        bitcoin(respect, status)



def slow_wifi(respect, status):
    pass


def servers_down(respect, status):
    pass


def online_textbook(respect, status):
    minor_issue = Room_251.check_computers("can\'t access online textbook", room_251)
    if minor_issue == "chat gpt":
        chatgpt(respect, status)
        room_251.remove("chat gpt")
    elif minor_issue == "roblox":
        roblox(respect, status)
        room_251.remove("roblox")
    elif minor_issue == "food":
        food(respect, status)
        room_251.remove("food")
    elif minor_issue == "bitcoin":
        bitcoin(respect, status)
        room_251.remove("bitcoin")


def wiped_hard_drives(respect, status):
    pass

def monitor_computers():
    minor_issue = Room_251.check_computers("none", room_251)


issues = ["software_unaccess", "slow_wifi", "servers_down", "online_textbook",
          "wiped_hard_drives"]

# software_unaccess(respect_level, status_level)
# software_unaccess(respect_level, status_level)

