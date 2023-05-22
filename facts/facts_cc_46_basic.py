class Facts:
    def __init__(self, victim_name, offence_date, jurisdiction, actions=None):
        self.victim_name = victim_name
        self.offence_date = offence_date
        self.jurisdiction = jurisdiction
        self.actions = actions if actions is not None else []

