"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ciara Weldon
Date: 10-22-2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    gold = 100

    # Use calculate_stats() to get stats
    strength, magic, health = calculate_stats(character_class, level)

    # Return character dictionary with exact key names
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


def calculate_stats(character_class, level):
    character_class = character_class.lower()

    if character_class == "warrior":
        strength = 5 + level * 3
        magic = 10 + level
        health = 20 + level * 2
    elif character_class == "mage":
        strength = 3 + level
        magic = 15 + level * 3
        health = 15 + level * 3
    elif character_class == "rogue":
        strength = 3 + level * 2
        magic = 12 + level
        health = 15 + level * 3
    elif character_class == "cleric":
        strength = 4 + level
        magic = 15 + level
        health = 15 + level * 4
    else:
        strength = magic = health = 0

    return strength, magic, health




    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

def load_character(filename):

"""
Used AI here to help update the dictionary
"""
    file = open(filename, "r")     # open file
    lines = file.readlines()       # read all lines
    file.close()                   # close file

    character = {}

    for line in lines:
        key, value = line.strip().split(":")   #
        character[key] = value

    return character
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """


    # TODO: Implement this function
    # Remember to handle file not found errors
    pass


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)

    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
        print("=== CHARACTER SHEET ===")  #prints the character info
        print(f"Name: {character['name']}")
        print(f"Class: {character['class']}")
        print(f"Level: {character['level']}")
        print(f"Strength: {character['strength']}")
        print(f"Magic: {character['magic']}")
        print(f"Health: {character['health']}")
        print(f"Gold: {character['gold']}")

    # TODO: Implement this function
    pass


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] += 1

    # Recalculate stats using the updated level
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up and is now {character['level']}!")
    print(f"New stats - Strength: {strength}, Magic: {magic}, Health: {health}")

    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")



