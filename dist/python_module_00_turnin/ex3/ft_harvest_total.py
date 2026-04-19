def ft_harvest_total():

    day: int = 1
    total: int = 0
    while day < 3:
        print(f"Day {day} harvest: ")
        usr_in: int = int(input())
        total += usr_in
        day += 1

    print(f"Total harvest: {total}")
