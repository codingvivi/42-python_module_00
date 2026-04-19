def ft_count_harvest_recursive():
    print("Days until harvest")
    usr_in: int = int(input())

    def print_days(num: int):
        if num == 1:
            print(f"Day {num}")
        else:
            print_days(num - 1)
            print(f"Day {num}")

    print_days(usr_in)
    print("Harvest time!")
