# High treason actions
HIGH_TREASON_ACTIONS = [("sovereign", ["kill"]), 
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

# Rules
def high_treason_rules(facts):
    """
    Checks if the facts of the case make out the offence of high treason.
    """
    # Check if any of the actions in the facts are in the list of high treason actions
    for action in facts.actions:
        for high_treason_action in HIGH_TREASON_ACTIONS:
            if action[0] == high_treason_action[0] and action[1] == high_treason_action[1]:
                return True

    return False