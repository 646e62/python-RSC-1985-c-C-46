'''
Rules determining whether a factual matrix corresponds to offence elements.
'''

import rules_constants

# High treason
## Actions

## Rules
def high_treason_rules(facts):
    """
    Checks if the facts of the case make out the offence of high treason.
    """
    # Check if any of the actions in the facts are in the list of high treason actions
    for action in facts.actions:
        for high_treason_action in rules_constants.HIGH_TREASON_ACTIONS:
            if action[0] == high_treason_action[0] and action[1] == high_treason_action[1]:
                return True

    return False

# Treason
## Actions

