from energy_source import *

input_info = "SolarPanel Area 20 Efficiency 15"

param = input_info.split(" ")
kwargs = {}
for i in range(1, len(param), 2):
    key = param[i].lower()
    value = param[i + 1]
    if value.isdigit():
        kwargs[key] = float(value)
    else:
        kwargs[key] = value

class_instance = globals()[param[0]](**kwargs)

result = class_instance.energy_output()
print(result)