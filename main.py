"""
Houses the code that executes the program. This is the file that should be run
to start the program. It is responsible for creating the Facts object that
contains the facts of the case, and then passing it to the rule base to be
evaluated. It then prints the result of the rule base evaluation.

It's currently limited to high treason offences, but could be expanded to
include other offences.
"""

from facts import high_treason_facts
from rules import high_treason_rules
from models import Facts
from input_correction import standardize_sovereign_names, standardize_canada_names


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

facts = create_facts()

if high_treason_rules(facts):
    print("High treason committed.")
else:
    print("No offence detected.")