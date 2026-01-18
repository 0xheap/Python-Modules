# Python OOP Complete Guide - CodeCultivation

## Table of Contents
1. [Basic Program Structure](#1-basic-program-structure)
2. [Classes & Objects](#2-classes--objects)
3. [The `self` Keyword](#3-the-self-keyword)
4. [Methods](#4-methods)
5. [Inheritance](#5-inheritance)
6. [super() Function](#6-super-function)
7. [Special Methods](#7-special-methods)
8. [Static Methods](#8-static-methods)
9. [Class Methods](#9-class-methods)
10. [Nested Classes](#10-nested-classes)
11. [isinstance() Function](#11-isinstance-function)
12. [Class vs Instance Variables](#12-class-vs-instance-variables)
13. [f-strings](#13-f-strings)
14. [Variable Arguments (*args)](#14-variable-arguments-args)

---

## 1. Basic Program Structure

### `if __name__ == "__main__":`

**Ash howa?**
Special condition li katgoul: "run had code ghir ila kant8dem file directly"

**3lash kayn?**
- Ki tat8dem file directly: `python3 file.py`, `__name__` = `"__main__"`
- Ki tat import file f file akhor, `__name__` = file name
- Katkhlik code yakhdem ghir ki bghiti

**Example:**
```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()  # Runs only when file executed directly
```

---

## 2. Classes & Objects

### Ash howa Class?
Class howa **blueprint** wla **template** bach tdir objects.

### Ash howa Object?
Object howa **instance** mn class - shi Haja real li kat create mn blueprint.

**Real-world analogy:**
- Class = Cookie cutter (9alib)
- Object = Cookie li khrejti mn 9alib

**Example:**
```python
# Class definition (blueprint)
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

# Objects (instances)
rose = Plant("Rose", 25)      # Object 1
cactus = Plant("Cactus", 15)  # Object 2
```

**3lash kat use classes?**
- Organization - keeps related data w functions together
- Reusability - create multiple objects mn same blueprint
- No code duplication

---

## 3. The `self` Keyword

### Ash howa `self`?
`self` howa reference l object li kat8dem 3lih daba. Bhal "ana" dial object.

### 3lash kayn?
- Bach Python y3ref anhi object kat8dem 3lih
- Bach kol object ykoun 3ando data dyalo separate

**Example:**
```python
class Plant:
    def __init__(self, name, height):
        self.name = name      # "ana smiti name"
        self.height = height  # "ana touli height"
    
    def grow(self):
        self.height += 1      # "ana ghadi nzid 1 f touli dyali"

rose = Plant("Rose", 25)
cactus = Plant("Cactus", 15)

print(rose.name)    # "Rose" - data dial rose
print(cactus.name)  # "Cactus" - data dial cactus
```

**Important:**
- `self` is automatic - Python kay3tih automatically
- `self` dima first parameter f methods
- `self.attribute` bach taccessi data dial object

---

## 4. Methods

### Ash howa Method?
Function defined inside class. Behavior dial object.

### Types of Methods:

| Type | First Param | When to Use |
|------|-------------|-------------|
| Instance method | `self` | Needs instance data |
| Class method | `cls` | Needs class data |
| Static method | none | Pure utility |

**Example:**
```python
class Plant:
    def __init__(self, name, height):  # Instance method
        self.name = name
        self.height = height
    
    def grow(self):  # Instance method
        self.height += 1
```

---

## 5. Inheritance

### Ash howa Inheritance?
Class jdida li kat **inherit** (kat werreth) kol shi mn class okhra w kat zid features dyalha.

**Real-world analogy:**
- Plant = Animal
- FloweringPlant = Dog
- Dog IS an Animal, but has extra features

**Syntax:**
```python
class ChildClass(ParentClass):
    pass
```

**Example:**
```python
# Parent class
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def grow(self):
        self.height += 1

# Child class
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)  # Call parent
        self.color = color              # Add new attribute
        self.blooming = True

# FloweringPlant gets: name, height, grow() + color, blooming
rose = FloweringPlant("Rose", 25, "red")
rose.grow()  # Inherited from Plant!
```

### Inheritance Chain:
```
Plant → FloweringPlant → PrizeFlower

PrizeFlower gets:
├── From Plant: name, height, grow()
├── From FloweringPlant: color, blooming
└── Own: points
```

---

## 6. super() Function

### Ash howa `super()`?
`super()` kat call method mn **parent class**.
it follow **Method Resolution Order (MRO)!**
- feauters :

### 1. Flexibility & Maintainability

```python
# BAD - Hardcoded class name:
class CC(CB):
    def method(self):
        CB.method(self)  # Hardcoded "CB"
```
### If you change inheritance: CC(NewParent)
### You must manually change CB.method(self) → NewParent.method(self)

```python
# GOOD - Dynamic:
class CC(CB):
    def method(self):
        super().method()  # Automatically finds correct parent
```
**If you change inheritance: CC(NewParent)**
**super() automatically calls NewParent.method() - no code change needed!**
### 3lash kayn?
Bach ma t3awedch code li already kayn f parent.

**Example:**
```python
# Without super() - BAD (code duplication)
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        self.name = name      # Repeating!
        self.height = height  # Repeating!
        self.color = color

# With super() - GOOD
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)  # Let parent handle this
        self.color = color              # Only add new stuff
```

---

## 7. Special Methods

### `__init__(self, ...)`
**Constructor** - kat8dem ki kat create object jdid.

```python
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

rose = Plant("Rose", 25)  # __init__ called automatically
```

### `__str__(self)`
Kat define how object yt **print**.

```python
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def __str__(self):
        return f"{self.name}: {self.height}cm"

rose = Plant("Rose", 25)
print(rose)  # "Rose: 25cm" (not <Plant object at 0x...>)
```

---

## 8. Static Methods

### Ash howa @staticmethod?
Method li **makatHtajch** `self` wla `cls`. Pure utility function.

### 3lash kayn?
- Functions li related l class walakin makatHtajch instance data
- Same result kol merra - no state needed

**Syntax:**
```python
@staticmethod
def method_name(params):
    # No self, no cls
    pass
```

**Example:**
```python
class Plant:
    @staticmethod
    def validate_height(height):
        return height > 0

# Call without creating object
Plant.validate_height(25)   # True
Plant.validate_height(-5)   # False
```

---

## 9. Class Methods

### Ash howa @classmethod?
Method li katakhod `cls` (class itself) instead of `self` (instance).

### 3lash kayn?
- Operations 3la class level
- Alternative constructors
- Access class variables

**Syntax:**
```python
@classmethod
def method_name(cls, params):
    # cls = the class itself
    pass
```

**Example:**
```python
class GardenManager:
    total_gardens = 0
    
    def __init__(self, owner):
        self.owner = owner
        GardenManager.total_gardens += 1
    
    @classmethod
    def get_total_gardens(cls):
        return cls.total_gardens
    
    @classmethod
    def create_garden_network(cls, *names):
        return [cls(name) for name in names]

# Usage
alice, bob = GardenManager.create_garden_network("Alice", "Bob")
print(GardenManager.get_total_gardens())  # 2
```

### 3lash `cls` machi class name?
- More flexible
- Ila class inherit, ghadi ykhdem correctly

---

## 10. Nested Classes

### Ash howa Nested Class?
Class defined **inside** class okhra.

### 3lash kayn?
- Helper class li ma3andoch meaning outside parent
- Organization - keeps related code together
- Encapsulation

**Real-world analogy:**
Engine inside Car - Engine ma3andoch meaning bla Car.

**Example:**
```python
class GardenManager:
    
    class GardenStats:  # Nested class
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
        
        def update_growth(self, amount):
            self.total_growth += amount
    
    def __init__(self, owner):
        self.owner = owner
        self.stats = self.GardenStats()  # Create nested class instance
```

---

## 11. isinstance() Function

### Ash howa isinstance()?
**Built-in function** li kat check wach object mn type m3ayan.

### Syntax:
```python
isinstance(object, ClassName)  # Returns True or False
```

**Example:**
```python
rose = FloweringPlant("Rose", 25, "red")
prize = PrizeFlower("Lily", 30, "white")

isinstance(rose, FloweringPlant)   # True
isinstance(rose, Plant)            # True (inheritance!)
isinstance(prize, PrizeFlower)     # True
isinstance(prize, FloweringPlant)  # True (inheritance!)
isinstance(prize, Plant)           # True (inheritance!)
```

### Order Matters!
```python
# WRONG - PrizeFlower never detected
if isinstance(plant, FloweringPlant):
    print("flowering")
elif isinstance(plant, PrizeFlower):  # Never reached!
    print("prize")

# CORRECT - Most specific first
if isinstance(plant, PrizeFlower):
    print("prize")
elif isinstance(plant, FloweringPlant):
    print("flowering")
else:
    print("regular")
```

### isinstance() vs type():
```python
rose = FloweringPlant("Rose", 25, "red")

type(rose) == FloweringPlant  # True
type(rose) == Plant           # False (exact match only)

isinstance(rose, FloweringPlant)  # True
isinstance(rose, Plant)           # True (checks inheritance!)
```

---

## 12. Class vs Instance Variables

### Instance Variables:
- Defined with `self.variable`
- **Specific** to each object
- Different value for each instance

### Class Variables:
- Defined **outside** `__init__`
- **Shared** by all instances
- Same value for all objects

**Example:**
```python
class GardenManager:
    total_gardens = 0  # Class variable (shared)
    
    def __init__(self, owner):
        self.owner = owner  # Instance variable (specific)
        self.plants = []    # Instance variable (specific)
        GardenManager.total_gardens += 1  # Modify class variable

alice = GardenManager("Alice")
bob = GardenManager("Bob")

print(alice.owner)  # "Alice" (instance)
print(bob.owner)    # "Bob" (instance)
print(GardenManager.total_gardens)  # 2 (shared)
```

---

## 13. f-strings

### Ash howa f-string?
**Formatted string** - bach t insert variables inside string.

### Syntax:
```python
f"text {variable} more text"
```

**Example:**
```python
name = "Rose"
height = 25

# Without f-string
print("Plant: " + name + ", Height: " + str(height))

# With f-string (cleaner!)
print(f"Plant: {name}, Height: {height}cm")
```

### Important:
```python
# Wrong - literal text
print("{name}: {height}cm")  # Output: {name}: {height}cm

# Correct - f-string
print(f"{name}: {height}cm")  # Output: Rose: 25cm
```

### Multi-line f-string (for flake8):
```python
# Line too long? Use parentheses:
return (
    f"{self.name}: {self.height}cm, "
    f"{self.color} flowers"
)
```

---

## 14. Variable Arguments (*args)

### Ash howa *args?
Kat accept **variable number** of arguments.

### Syntax:
```python
def function(*args):
    # args is a tuple
    for arg in args:
        print(arg)
```

**Example:**
```python
@classmethod
def create_garden_network(cls, *owner_names):
    return [cls(name) for name in owner_names]

# Can call with any number of arguments:
GardenManager.create_garden_network("Alice")
GardenManager.create_garden_network("Alice", "Bob")
GardenManager.create_garden_network("Alice", "Bob", "Charlie")
```

---

## Quick Reference Table

| Concept | Syntax | Purpose |
|---------|--------|---------|
| Class | `class Name:` | Blueprint for objects |
| Object | `obj = Class()` | Instance of class |
| self | `self.attr` | Reference to current object |
| Inheritance | `class Child(Parent):` | Inherit from parent |
| super() | `super().__init__()` | Call parent method |
| @staticmethod | `@staticmethod` | Utility function |
| @classmethod | `@classmethod` | Class-level operation |
| isinstance() | `isinstance(obj, Class)` | Type checking |
| \_\_init\_\_ | `def __init__(self):` | Constructor |
| \_\_str\_\_ | `def __str__(self):` | String representation |

---

## Final Project Structure

```
Plant (base)
├── name, height
├── grow()
└── validate_height() [@staticmethod]

FloweringPlant (inherits Plant)
├── color, blooming
└── __str__()

PrizeFlower (inherits FloweringPlant)
├── points
└── __str__()

GardenManager
├── total_gardens [class variable]
├── GardenStats [nested class]
│   ├── plants_added, total_growth, plant_types
│   ├── update_growth()
│   └── add_plant()
├── __init__()
├── add_plant()
├── grow_all_plants()
├── get_total_score()
├── generate_report()
├── create_garden_network() [@classmethod]
└── get_total_gardens() [@classmethod]
```

---

**Mabrouk! You completed CodeCultivation! 🎉**
