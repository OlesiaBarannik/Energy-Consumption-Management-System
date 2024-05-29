class EnergySource:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def energy_output(self):
        return f"{self.__class__.__name__} AnnualEnergyOutput {round(self.get_result())}"


class SolarPanel(EnergySource):

    def get_result(self, k=15):
        self.k = k
        return self.area * self.efficiency * self.k


class WindTurbine (EnergySource):

    def get_result(self, k=150):
        self.k = k
        return self.height * self.windspeedaverage * self.k


class HydroPlant(EnergySource):

    def get_result(self, k=12):
        self.k = k
        return self.flowrate  * self.drop * self.k


class OffshoreWindTurbine(EnergySource):

    def get_result(self, k=160):
        self.k = k
        return self.height  * self.windspeedaverage * (1 - self.corrosionfactor) * self.k
