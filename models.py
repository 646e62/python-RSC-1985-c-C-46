class Facts:
    """
    A basic class capable of handling the minimum facts required for a high treason offence.
    """
    def __init__(self, victim_name, offence_date, jurisdiction, actions=None):
        self.victim_name = victim_name
        self.offence_date = offence_date
        self.jurisdiction = jurisdiction
        self.actions = actions if actions is not None else []

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
