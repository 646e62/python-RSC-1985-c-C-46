'''
Test project for designing an expert system that can work with the Canadian 
Criminal Code. 
'''

# Step one is to create an object containing everything that needs to be tested

class Offence:
    '''
    The Offence class should contain all of the information about a given
    offence. 
    '''
    def __init__(self, name):
        self.name = name
        print(f"Initialized with name: {self.name}")
        
