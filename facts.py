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

# Actions

def get_sovereign_actions():
    """
    Ask the user questions related to actions against the sovereign.
    """
    attack_on_sovereign_actions = [
        ("Did the defendant kill the king?", ["kill"]),
        ("Did the defendant attempt to kill the king?", ["kill", "attempt"]),
        ("Did the defendant do bodily harm to the king tending to death?", ["bodily harm", "tending to death"]),
        ("Did the defendant do bodily harm to the king tending to destruction?", ["bodily harm", "tending to destruction"]),
        ("Did the defendant maim the king?", ["maim"]),
        ("Did the defendant wound the king?", ["wound"]),
        ("Did the defendant imprison the king?", ["imprison"]),
        ("Did the defendant restrain the king?", ["restrain"])
    ]

    actions = []
    for question in attack_on_sovereign_actions:
        response = input(question[0] + " (yes/no): ")
        if response.lower() == 'yes':
            actions.append(("sovereign", question[1]))
    
    return actions

def get_canada_actions():
    """
    Ask the user questions related to actions against Canada.
    """
    war_against_canada_actions = [
        ("Did the defendant levy war against Canada?", ["levy war"]),
        ("Did the defendant prepare to levy war against Canada?", ["prepare", "levy war"]),
        ("Did the defendant assist an enemy at war with Canada?", ["assist warring enemy"]),
        ("Did the defendant assist an armed force hostily engaged with Canadian Forces?", ["assist hostile force"])
    ]

    actions = []
    for question in war_against_canada_actions:
        response = input(question[0] + " (yes/no): ")
        if response.lower() == 'yes':
            actions.append(("canada", question[1]))

    return actions

# Facts

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
