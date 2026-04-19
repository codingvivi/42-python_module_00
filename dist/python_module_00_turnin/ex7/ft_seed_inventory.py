def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    readout: str = seed_type.title()

    readout += " seeds: "

    match unit:
        case "packets":
            readout += f"{quantity} {unit} available"
        case "grams":
            readout += f"{quantity} {unit} total"
        case "area":
            readout += f"covers {quantity} square meters"
        case _:
            readout = "Unknown unit type"
    print(readout)
