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