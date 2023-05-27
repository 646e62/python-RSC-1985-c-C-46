'''
Constants used in the statutory rules.
'''

# High treason
HIGH_TREASON_RULES = {
    "sovereign": [("Did the defendant kill the sovereign?",
                   ["kill"]),
                  ("Did the defendant attempt to kill the sovereign?",
                   ["kill", "attempt"]),
                  ("Did the defendant do bodily harm to the sovereign tending to death?",
                   ["bodily harm", "tending to death"]),
                  ("Did the defendant do bodily harm to the sovereign tending to destruction?",
                   ["bodily harm", "tending to destruction"]),
                  ("Did the defendant maim the sovereign?",
                   ["maim"]),
                  ("Did the defendant wound the sovereign?",
                   ["wound"]),
                  ("Did the defendant imprison the sovereign?",
                   ["imprison"]),
                  ("Did the defendant restrain the sovereign?",
                   ["restrain"])],
    "canada": [("Did the defendant levy war against Canada?",
                ["levy war"]),
               ("Did the defendant prepare to levy war against Canada?",
                ["prepare", "levy war"]),
               ("Did the defendant assist an enemy at war with Canada?",
                ["assist warring enemy"]),
               ("Did the defendant assist an armed force hostily engaged with Canadian Forces?",
                ["assist hostile force"])]}

# Treason
TREASON_ACTIONS = [("canada", ["specific intent", "use force", "overthrow government"]),
                   ("canada", ["specific intent", "use violence", "overthrown government"]),
                   ("province", ["specific intent", "use force", "overthrow government"]),
                   ("province", ["specific intent", "use violence", "overthrown government"]),
                   ]