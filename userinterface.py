

def collect_contestant_info():
    """use this main menu to allow a company to collect registrant info"""
    peron_is_not_current_contestant = (True, None)
    while peron_is_not_current_contestant[0] is True:
        print("Are you a current contestant? Please enter Yes or No")
        first_name = input("First Name:")
        last_name = input("Last Name:")
        email = input("Email Address:")
        print("You have been registered for this contest!")
        peron_is_not_current_contestant = peron_is_not_current_contestant(input)
        return

    person_is_previous_contestant = True
    while person_is_previous_contestant[0] is True:
        email = input("Email Address:")
        print("Welcome Back! You have been registered for this contest!")

def validate_main_menu(input):
    switcher = {
        Yes: True,
        No: False
    }
    return switcher.get(input)