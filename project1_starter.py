"""
COMP 163 - Project 1: Character Creator
Name: Ciara Weldon
Date: 10-22-2025

AI Usage:
AI helped correct formatting and logic in load_character and display_character functions,
and assisted cleaning comments.
"""


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1  # default starting level
    gold = 100  # default starting gold

    # Use calculate_stats() to get stats based on class & level
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
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)

    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """

    character_class = character_class.lower()  # make class lowercase so matching works

    # stat formulas for each class
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
        strength = magic = health = 0  # invalid class case

    return strength, magic, health



def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful
    """
    import os

    if not isinstance(character, dict) or not filename:
        return False

    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    return True


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful
    """
    import os
    if not os.path.exists(filename):
        return None
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}

    for line in lines:
        line = line.strip()
        key, value = line.split(": ")

        if key == "Character Name":
            character["name"] = value
        else:
            real_key = key.lower()
            if real_key in ["level", "strength", "magic", "health", "gold"]:
                character[real_key] = int(value)
            else:
                character[real_key] = value

    return character



def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """

    print("=== CHARACTER SHEET ===")  # prints the character info
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """

    character["level"] += 1  # increase level by 1

    # Recalculate stats using the updated level
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up and is now level {character['level']}!")
    print(f"New stats - Strength: {strength}, Magic: {magic}, Health: {health}")


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Example usage (uncomment to test):
    # char = create_character("Aria", "Mage")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
    # display_character(loaded)
    # level_up(loaded)


