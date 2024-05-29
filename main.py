from energy_source import *

input_info = "OffshoreWindTurbine Height 70 WindSpeedAverage 8 CorrosionFactor 0.2"

param = input_info.split(" ")
kwargs = {}
for i in range(1, len(param), 2):
    key = param[i].lower()
    kwargs[key] = float(param[i + 1])

class_instance = globals()[param[0]](**kwargs)

result = class_instance.energy_output()
print(result)