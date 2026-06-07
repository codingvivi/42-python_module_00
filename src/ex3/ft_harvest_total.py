def ft_harvest_total():

    day: int = 1
    total: int = 0
    while day <= 3:
        usr_in: int = int(input(f"Day {day} harvest: "))
        total += usr_in
        day += 1

    print(f"Total harvest: {total}")
