'''
Generates a factual matrix that can be used to determine whether the facts of
the case make out a particular offence.
'''

import rules_constants

# Defendant role: principal, party, accessory after the fact, attempt, conspiracy
def establish_party_liability():
    """
    Qualifies party liability by type. Presumes knowledge of the different types
    of party liability.
    """
    print("Party liability type (aider, abettor, common intention)? ")

    party_liability_type = input("Type: ")
    
    party_liability_types = ["aider", "abettor", "common intention"]

    if party_liability_type.lower() not in party_liability_types:
        print("Invalid party liability type.")
        return establish_party_liability()
    else:
        return party_liability_type.lower()
    

def establish_liability():
    """
    Determines whether the defendant is liable for the offence as a principal,
    party, accessory after the fact, attempt, or conspiracy. Or not at all. The
    function should return as soon as one role is established. 
    """

    print("What role did the defendant play in the offence? (principal, party, accessory after the fact, attempt, conspiracy, none)")
    role = input("Role: ")

    roles = ["principal", "party", "accessory after the fact", "attempt", "conspiracy", "none"]

    if role.lower() not in roles:
        print("Invalid role.")
        return establish_liability()
    elif role.lower() == "party":
        return establish_party_liability()
    else:
        return role.lower()


# High treason
## Actions
def get_sovereign_actions():
    """
    Ask the user questions related to actions against the sovereign.
    """

    actions = []
    for question in rules_constants.HIGH_TREASON_RULES["sovereign"]:
        response = input(question[0] + " (yes/no): ")
        if response.lower() == 'yes':
            actions.append(("sovereign", question[1]))
    
    return actions


def get_canada_actions():
    """
    Ask the user questions related to actions against Canada.
    """

    actions = []
    for question in rules_constants.HIGH_TREASON_RULES["canada"]:
        response = input(question[0] + " (yes/no): ")
        if response.lower() == 'yes':
            actions.append(("canada", question[1]))

    return actions


## Facts
def high_treason_facts(victim_name):
    """
    Asks the user questions to determine if the facts of the case make out the offence of high treason.
    """
    actions = []

    if victim_name.lower() == 'sovereign':
        actions = get_sovereign_actions()
    elif victim_name.lower() == 'canada':
        actions = get_canada_actions()

    return actions
