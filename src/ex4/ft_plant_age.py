def ft_plant_age():
    usr_in: int = int(input("Enter plant age in days: "))

    status: str = (
        "Plant is ready to harvest!"
        if usr_in > 60
        else "Plant needs more time to grow."
    )
    print(status)
