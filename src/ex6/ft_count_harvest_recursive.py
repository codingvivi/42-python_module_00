def ft_count_harvest_recursive():
    usr_in: int = int(input("Days until harvest: "))

    def print_days(num: int):
        if num == 1:
            print(f"Day {num}")
        else:
            print_days(num - 1)
            print(f"Day {num}")

    print_days(usr_in)
    print("Harvest time!")
