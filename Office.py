import variables


def office(stuxnet):
    print("You enter your office...\nDecide what to do:")
    while True:
        choice_correct = True
        print("1:Log onto teams\n2.Monitor student computers\n3.Monitor network\n4.Go for a walk")
        choice = input("What will you do?\n")
        if variables.error_check(choice, 4) is True:
            choice_correct = False
        while choice_correct is False:
            print("Enter a correct response\n1-4")
            choice = input("What will you do?\n")
            if variables.error_check(choice, 4) is True:
                choice_correct = False
            else:
                choice_correct = True

        if choice == "1":
            if stuxnet is False:
                crash = variables.rand_choice(0, 100, 25)
            if stuxnet is True:
                crash = variables.rand_choice(0, 100, 75)
            if crash is False:
                print("\n*sigh* Teams has crashed...\n")
                choice_correct = False
            print("You logged into teams")
        if choice_correct is True:
            break
    return choice


office(True)
