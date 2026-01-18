def ft_count_harvest_recursive(ran=None, value=1):
    if ran is None:
        ran = int(input("Days until harvest: "))
    print("Day", value)

    if value == ran:
        return

    return ft_count_harvest_recursive(ran, value + 1)
