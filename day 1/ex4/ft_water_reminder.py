def ft_water_reminder():
    Day = int(input("Days since last watering: "))
    if Day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
