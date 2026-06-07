def ft_count_harvest_iterative():
    usr_in: int = int(input("Days until harvest: "))

    for day in range(1, usr_in + 1):
        print(f"Day {day}")

    print("Harvest time!")
