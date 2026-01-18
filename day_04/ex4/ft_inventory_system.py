"""
This program manages a game inventory system.
It analyzes item quantities and provides statistics about the inventory.
"""
import sys

def unique_items(inventory) -> int:
    """
    Counts how many different types of items are in the inventory.
    """
    unique = 0
    list = []
    for item in inventory :
        if item not in list :
            unique += 1
            list += [item]
    return unique

def total(args) :
    """
    Counts the total number of arguments.
    """
    count  = 0
    for arg in args :
        count += 1
    return count

def total_items(inventory: dict) -> int :
    """
    Adds up all item quantities in the inventory.
    """
    total = 0
    for value in inventory.values():
        total += value
    return total

def most_abundant(inventory) -> str:
    """
    Finds the item with the highest quantity.
    """
    most = 0
    name = None
    for key, value in inventory.items():
        if most < value :
            most = value
            name = key
    return f"{name} ({most} units)"

def last_abundant(inventory) -> str:
    """
    Finds the item with the lowest quantity.
    """
    last = 777777777777777777777
    name = None
    for key, value in inventory.items():
        if last > value :
            last = value
            name = key
    return f"{name} ({last} units)"

def moderate(inventory : dict) -> dict:
    """
    Returns the item with the highest quantity as a dictionary.
    """
    moderate_ = dict()
    max = 0
    for key in inventory.keys():
        if inventory[key] > max :
            max = inventory[key]
            moderate_= {key:max}
    return moderate_

def max_value(inventory: dict) -> int :
    """
    Finds the highest quantity value in the inventory.
    """
    max = 0
    for value in inventory.values():
        if max < value :
            max = value
    return max

def min_value(inventory: dict) -> int :
    """
    Finds the lowest quantity value in the inventory.
    """
    min = 777777777777777777777
    for value in inventory.values():
        if min > value :
            min = value
    return min

def scarce(inventory : dict) -> dict:
    """
    Returns all items that don't have the maximum quantity.
    """
    scarce_ = dict()
    for key in inventory.keys():
        if inventory[key] < max_value(inventory) :
            scarce_.update({key:inventory[key]})
    return scarce_

def restock(inventory) -> list :
    """
    Returns a list of items that need restocking (have minimum quantity).
    """
    need = []

    for key, value in inventory.items() :
        if value == min_value(inventory) :
            need += [key]
    return need

def validation(args) -> bool :
    """
    Checks if the command line arguments are valid.
    """
    if total(args) < 1:
        print("Usage: python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1")
        return False
    if total(args) == 1 :
        print("I need More Args, YOu only give one")
        return False
    for arg in args :
        if ":" not in arg :
            print(f"Error Invalid Formt for '{arg}' it must be 'key:value'")
            return False
    return True

def checking(inventory, name) -> bool :
    """
    Checks if an item exists in the inventory.
    """
    if name in inventory :
        return True
    return False

def main() -> None:
    """
    Main function that processes inventory data and shows statistics.
    """
    
    if not validation(sys.argv[1:]) :
        return
    print("=== Inventory System Analysis ===\n")
    
    inventory : dict = dict()
    for arg in sys.argv[1:] :
        name, quantity = arg.split(":")
        inventory[name] = int(quantity)
    print("Total items in inventory: ", total_items(inventory))
    print("Unique item types: ", unique_items(inventory))
    
    print("\n=== Current Inventory ===")
    for key, value in inventory.items() :
        percent = (value / total_items(inventory)) * 100
        print(f"{key}: {value} units ({percent:.1f}%)")
    
    print("\n=== Inventory Statistics ===")
    print("Most abundant:", most_abundant(inventory))
    print("Least abundant:", last_abundant(inventory))
    
    print("\n=== Item Categories ===")
    print("Moderate :", moderate(inventory))
    print("Scarce :", scarce(inventory))
    
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", restock(inventory))
    

    print("\n=== Dictionary Properties Demo ===")
    keys = []
    for key in inventory.keys() :
        keys += [key]
    print("Dictionary keys: ", keys)
    values = []
    for value in inventory.values() :
        values += [value]
    print("Dictionary values: ", values)
    name = "sworde"
    if checking(inventory, name) :
        print(f"Sample lookup - '{name}' in inventory: True")
    else :
        print(f"Sample lookup - '{name}' in inventory: False")
main()