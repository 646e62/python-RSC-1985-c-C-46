"""
Functions used to process input strings and correct them to a standard format.
"""

# High treason

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

# Treason

def treason_location_type(input_string: str) -> str:
    """
    This function helps determine whether a string entity is a province or a 
    federally-regulated territory for the purpose of determining whether a 
    defendant has committed treason.
    """
    input_string = input_string.replace('.', '')  # Remove periods from input

    # Dictionary mapping province names, abbreviations and territory names, abbreviations to their corresponding types
    locations = {
        "alberta": "province",
        "ab": "province",
        "alta": "province",
        "british columbia": "province",
        "bc": "province",
        "manitoba": "province",
        "mb": "province",
        "man": "province",
        "new brunswick": "province",
        "nb": "province",
        "newfoundland and labrador": "province",
        "nl": "province",
        "nova scotia": "province",
        "ns": "province",
        "ontario": "province",
        "on": "province",
        "ont": "province",
        "prince edward island": "province",
        "pei": "province",
        "quebec": "province",
        "qc": "province",
        "que": "province",
        "saskatchewan": "province",
        "sk": "province",
        "sask": "province",
        "northwest territories": "canada",
        "nt": "canada",
        "nwt": "canada",
        "nunavut": "canada",
        "nu": "canada",
        "nvt": "canada",
        "yukon": "canada",
        "yt": "canada"
    }

    # Return the corresponding value if the input string is in the dictionary, else return "Unknown"
    return locations.get(input_string.lower(), "Unknown")
