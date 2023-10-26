import re

def is_valid_name(name):
        # Check if the name contains only letters and is no more than 15 characters.
        pattern = r"^[a-zA-Z]{1,15}$"
        
        return bool(re.match(pattern, name))
class Character:
    name = ""

    def __init__(self, character_name):
        if is_valid_name(character_name):
            self.name = character_name
        else:
            self.name = ""

        # # Test the function with some example names
        # names = ["John", "Alice123", "Elizabeth Ann", "Bob_"]

        # for name in names:
        #     if is_valid_name(name):
        #         print(f"{name} is a valid name.")
        #     else:
        #         print(f"{name} is not a valid name.")

