def ft_count_harvest_iterative():
    print("Days until harvest")
    usr_in: int = int(input())

    for day in range(1, usr_in + 1):
        print(f"Day {day}")

    print("Harvest time!")
