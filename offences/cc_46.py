"""
Criminal Code s 46 contains two broad offences:

* High treason
* Treason

Both high treason and treason consist of several sub-offences. The
offences are defined in ss 46(1) and 46(2) respectively. The offences
are defined in terms of the following acts:

# High treason
## 46(1)(a) — Offence against the Sovereign
* Killing the king
* Attempting to kill the king
* Doing bodily harm to the king tending to death
* Doing bodily harm to the king tending to destruction
* Maiming the king
* Wounding the king
* Imprisoning the king
* Restraining the king

## 46(1)(b) — Levying war
* Levying war against Canada
* Preparing to levy war against Canada

## 46(1)(c) — Assisting an enemy
* Assisting an enemy at war with Canada
* Assiting an armed force hostily engaged with Canadian Forces

# Treason
## 46(2)(a) — Overthrowing the government
* Using force to overthrow the Canadian government
* Using force to overthrow a provincial government
* Using violence to overthrow the Canadian government
* Using violence to overthrow a provincial government

## 46(2)(b) — military secrets
* One or more of each of the following:
  * Nature: military or scientific
  * Medium: sketch, plan, model, article, note, document, information
  * Target: foreign state agent
  * Effect: prejudicial to: safety, defence

## 46(2)(c) — treason conspiracy
* Conspiracy to commit high treason
* Conspiracy to commit a 46(2)(b) offence

## 46(2)(d) — treason intention with overt act


## 46(2)(e) — military secret treason and intention with overt act

"""

# High treason

## Rules

def high_treason_rules(facts):
    """
    Checks if the facts of the case make out the offence of high treason.
    """
    # Actions that constitute high treason
    high_treason_actions = [("sovereign", ["kill"]), 
                            ("sovereign", ["kill", "attempt"]),
                            ("sovereign", ["bodily harm", "tending to death"]),
                            ("sovereign", ["bodily harm", "tending to destruction"]),
                            ("sovereign", ["maim"]), 
                            ("sovereign", ["wound"]),
                            ("sovereign", ["imprison"]), 
                            ("sovereign", ["restrain"]),
                            ("canada", ["levy_war"]), 
                            ("canada", ["prepare", "levy war"]),
                            ("canada", ["assist warring enemy"]), 
                            ("canada", ["assist hostile force"])]

    # Check if any of the actions in the facts are in the list of high treason actions
    
    for action in facts.actions:
        for high_treason_action in high_treason_actions:
            if action[0] == high_treason_action[0] and action[1] == high_treason_action[1]:
                return True

    return False


## Facts

def high_treason_facts(victim_name):
    """
    Asks the user questions to determine if the facts of the case make out the offence of high treason.
    """
    actions = []

    if victim_name.lower() == 'sovereign':
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

        for question in attack_on_sovereign_actions:
            response = input(question[0] + " (yes/no): ")
            if response.lower() == 'yes':
                actions.append(("sovereign", question[1]))

    elif victim_name.lower() == 'canada':
        war_against_canada_actions = [
            ("Did the defendant levy war against Canada?", ["levy war"]),
            ("Did the defendant prepare to levy war against Canada?", ["prepare", "levy war"]),
            ("Did the defendant assist an enemy at war with Canada?", ["assist warring enemy"]),
            ("Did the defendant assist an armed force hostily engaged with Canadian Forces?", ["assist hostile force"])
        ]

        for question in war_against_canada_actions:
            response = input(question[0] + " (yes/no): ")
            if response.lower() == 'yes':
                actions.append(("canada", question[1]))

    return actions


# Input correction

def standardize_sovereign_names(name):
    """
    This function takes a name and standardizes it to 'Sovereign' if it matches any of the known aliases.
    """
    known_aliases = ('queen', 'king', 'queen elizabeth', 'king charles')
    if name.lower() in known_aliases:
        return 'sovereign'
    else:
        return name

def standardize_canada_names(name):
    """
    This function takes a name and standardizes it to 'Canada' if it matches any of the known aliases.
    """
    known_aliases = ('nation of canada', 'canadian people', 'canadian military')
    if name.lower() in known_aliases:
        return 'canada'
    else:
        return name

# UI

def create_facts():
    """
    Creates a Facts object that can then be read using the rule base.
    """

    print("Please enter the facts of the case:")

    victim_name = input("Who is the victim? ")
    victim_name = standardize_sovereign_names(victim_name)
    victim_name = standardize_canada_names(victim_name)

    offence_date = input("Date of the offence (YYYY-MM-DD): ")
    jurisdiction = input("Jurisdiction: ")

    actions = high_treason_facts(victim_name)

    return Facts(victim_name, offence_date, jurisdiction, actions)

# Fact class

class Facts:
    """
    A basic class capable of handling the minimum facts required for a high treason offence.
    """
    def __init__(self, victim_name, offence_date, jurisdiction, actions=None):
        self.victim_name = victim_name
        self.offence_date = offence_date
        self.jurisdiction = jurisdiction
        self.actions = actions if actions is not None else []

# Program execution

facts = create_facts()

if high_treason_rules(facts):
    print("High treason committed.")
else:
    print("No offence detected.")
