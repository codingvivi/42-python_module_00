def ft_water_reminder():
    prompt: str = "Days since last watering: "
    print(prompt)

    usr_in: int = int(input())

    status: str = "Water the plants!" if usr_in > 2 else "Plants are fine"
    print(status)
