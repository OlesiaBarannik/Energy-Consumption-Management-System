from abc import ABC, abstractmethod


class EnergySource:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.validate()

    def energy_output(self):
        return f"{self.__class__.__name__} AnnualEnergyOutput {round(self.calculate_result())}"

    def validate(self):
        invalid_keys = []
        for key, value in self.__dict__.items():
            if not isinstance(value, (int, float)):
                invalid_keys.append(key)
        if invalid_keys:
            raise TypeError(f"{', '.join(invalid_keys)} must be a number.")

    @abstractmethod
    def calculate_result(self):
        pass


class SolarPanel(EnergySource):
    def calculate_result(self, k=15):
        return self.area * self.efficiency * k


class WindTurbine(EnergySource):
    def calculate_result(self, k=150):
        return self.height * self.windspeedaverage * k


class HydroPlant(EnergySource):
    def calculate_result(self, k=12):
        return self.flowrate * self.drop * k


class OffshoreWindTurbine(EnergySource):
    def calculate_result(self, k=160):
        return self.height * self.windspeedaverage * (1 - self.corrosionfactor) * k
