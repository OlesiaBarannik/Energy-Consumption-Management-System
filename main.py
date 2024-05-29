from energy_source import *

input_info = "WindTurbine Height 50 WindSpeedAverage 6"


param = input_info.split(" ")
kwargs = {}
for i in range(1, len(param), 2):
    key = param[i].lower()
    kwargs[key] = float(param[i + 1])

class_instance = globals()[param[0]](**kwargs)

result = class_instance.energy_output()
print(result)