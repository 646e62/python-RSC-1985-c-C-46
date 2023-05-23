class Facts:
    """
    A basic class capable of handling the minimum facts required for a high 
    treason offence.

    Attributes:
        victim_name (str): The name of the victim of the offence.
        offence_date (str): The date of the offence.
        jurisdiction (str): The jurisdiction in which the offence took place.
        actions (list): A list of actions that the defendant took against the 
            victim.
        role (list): A list of roles that the defendant played in the offence.

    A Facts object should account for one offence and offender. Any potential
    path to a conviction should be represented by a distinct Facts object. 
    Multiple offences or offenders should be represented by multiple Facts 
    objects.
    """

    def __init__(self, victim_name, offence_date, jurisdiction, actions=None, role=None):
        self.victim_name = victim_name
        self.offence_date = offence_date
        self.jurisdiction = jurisdiction
        self.actions = actions if actions is not None else []
        self.role = role if role is not None else []

class Complainant:
    """
    Creates a complainant instance. Necessary to the extent that some offences 
    only apply to complainants with certain characteristics, and to the extent
    that some offences will involve multiple complainants who need to be kept
    distinct from one another.
    """
    def __init__(self, name=None, age=None, type=None):
        self.name = name
        self.age = age
        self.type = type

class Defendant:
    """
    Creates a defendant instance. Necessary to the extent that some offences 
    only apply to defendants with certain characteristics, and to the extent
    that some offences will involve multiple defendants who need to be kept
    distinct from one another.
    """
    def __init__(self, name=None, age=None, liability=None):
        self.name = name
        self.age = age
        self.liability = liability
    
    # Rather than giving Defendant a liability attribute, it might be better to
    # relegate liability to 