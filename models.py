class Facts:
    """
    A basic class capable of handling the minimum facts required for a high treason offence.
    """
    def __init__(self, victim_name, offence_date, jurisdiction, actions=None):
        self.victim_name = victim_name
        self.offence_date = offence_date
        self.jurisdiction = jurisdiction
        self.actions = actions if actions is not None else []