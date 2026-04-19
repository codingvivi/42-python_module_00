def ft_plot_area():

    def get_dimension(side: str) -> int:

        prompt: str = f"Enter {side}: "
        print(prompt)

        return int(input())

    length: int = get_dimension("length")
    width: int = get_dimension("width")

    size: int = length * width
    plot_msg: str = f"Plot area: {size}"

    print(plot_msg)
