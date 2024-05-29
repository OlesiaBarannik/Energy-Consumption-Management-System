from energy_source import *

def parse_input_info(input_info):
    param = input_info.split(" ")
    kwargs = {}
    for i in range(1, len(param), 2):
        key = param[i].lower()
        value = param[i + 1]
        try:
            kwargs[key] = float(value)
        except ValueError:
            kwargs[key] = value

    return param[0], kwargs


def main():
    input_info = input("Enter the energy source and its parameters (e.g., 'SolarPanel Area 20 Efficiency 15'): ")
    class_instance_name, kwargs = parse_input_info(input_info)

    try:
        class_instance = globals()[class_instance_name](**kwargs)
        result = class_instance.energy_output()
        print(result)
    except KeyError:
        print(f"Invalid energy source name {class_instance_name}")


if __name__ == "__main__":
    main()
