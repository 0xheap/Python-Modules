## NOTES FOR CLASSES IN PYTHON
-------------------------------
Blueprint = mokhatat wlla template

Example:
- Ila bghiti tebni dar, khassek mokhatat (blueprint) li katbeyyen: feen l bit, feen l salon, feen l cuisine...
- Mn nafs l mokhatat, tqeder tebni 100 dour, kol wa7da fiha nafs l structure walaken colors w furniture mokhtlf.

F Python:
- **Class** = mokhatat/blueprint
- **Object** = dar li bniti mn l mokhatat

Example:
```python
class Plant:  # Hadi mokhatat dyal nabta
    def __init__(self, name, height, age):
        self.name = name
        self.height = height  
        self.age = age

# Hna kandiro plants (objects) mn nafs l mokhatat:
rose = Plant("Rose", 25, 30)        # Nabta 1
sunflower = Plant("Sunflower", 80, 45)  # Nabta 2  
cactus = Plant("Cactus", 15, 120)       # Nabta 3
```

Kol nabta 3andha nafs l structure (name, height, age) walaken values mokhtlfa.

Blueprint/mokhatat = l structure li ghadi tkoun 3and kol object.

- self howa reference l object li kat8dem 3lih daba.



// Exercise 2 :
### Key concepts hna:
1. Methods modify object: grow() w age_one_day() katbedlou self.height w self.age
2. Object state changes: Nafs object, walakin values dyalo katbedel over time
3. Encapsulation: Logic dial growth w aging kayn inside object, machi outside

// ex 4 :
### Mafhum jdid: Getters w Setters

Ash homa?
- **Getter:** Method li kat3tik value dial attribute (controlled reading)
- **Setter:** Method li katبدل value dial attribute (controlled writing)

3lash nst3mlou-hom?
- Bach nvalidatiw data 9bel storage
- Bach n7miw attributes mn direct access
- Bach ndirou error handling


name mangling in python












# Exercise 6: Garden Analytics Platform

### Chno khasna ndiro?
Khasna ndirou comprehensive system li kay manage multiple gardens w kay3ti analytics. Hadi exercise li katjme3 kol shi 
t3lemna-h!

### Mfahim jdida f hadi exercise:

### 1. Nested Classes
Ash howa?
Class inside class akhor. Bhal room inside house.

3lash kayn?
- Bach torganize related functionality
- Bach tdir helper classes li ma3andhomch meaning outside parent class

Real-world analogy:
Bhal engine inside car - engine ma3andoch meaning bla car, walakin car 3ando bzaf dial components inside

### 2. Static Methods (@staticmethod)
Ash howa?
Method li makatHtajch self wla cls. Utility function inside class.

3lash kayn?
- Bach tdir functions li related l class walakin makatHtajch instance data
- Bhal calculator functions - same result kol merra

### 3. Class Methods (@classmethod)
Ash howa?
Method li katakhod cls (class itself) instead of self (instance).

3lash kayn?
- Bach tdir operations 3la class level
- Bach tdir alternative constructors

### Solution step by step:
