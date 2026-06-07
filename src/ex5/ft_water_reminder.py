def ft_water_reminder():
    usr_in: int = int(input("Days since last watering: "))

    status: str = "Water the plants!" if usr_in > 2 else "Plants are fine"
    print(status)
