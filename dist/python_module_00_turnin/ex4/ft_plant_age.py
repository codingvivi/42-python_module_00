def ft_plant_age():
    prompt: str = "Enter plant age in days: "
    print(prompt)

    usr_in: int = int(input())

    status: str = (
        "Plant is ready to harvest!"
        if usr_in > 60
        else "Plant needs more time to grow."
    )
    print(status)
