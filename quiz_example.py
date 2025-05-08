def convert_celsius_to_kelvin(celsius):
    """
    Converts a temperature value from Celsius to Kelvin.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius + 273.15


if __name__ == "__main__":
    example = 25
    result = convert_celsius_to_kelvin(example)
    print(f"{example}°C is {result} K")
