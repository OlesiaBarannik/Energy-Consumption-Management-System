from abc import ABC, abstractmethod

class ResourceDepletionRateCalculateError(Exception):
    pass


class EnergySource:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.validate()

    def energy_output(self):
        return (f"{self.__class__.__name__} AnnualEnergyOutput {round(self.calculate_annual_energy_output())} "
                f"ResourceDepletionRate {round(self.calculate_resource_depletion_rate(), 2)}")

    def validate(self):
        invalid_keys = []
        for key, value in self.__dict__.items():
            if not isinstance(value, (int, float)):
                invalid_keys.append(key)
        if invalid_keys:
            raise TypeError(f"{', '.join(invalid_keys)} must be a number.")

    @abstractmethod
    def calculate_annual_energy_output(self):
        pass

    @abstractmethod
    def calculate_resource_depletion_rate(self):
        pass


class SolarPanel(EnergySource):
    def calculate_annual_energy_output(self, k=15):
        return self.area * self.efficiency * k

    def calculate_resource_depletion_rate(self, k=100):
        if self.efficiency <= 0:
            raise ResourceDepletionRateCalculateError
        return k / self.efficiency


class WindTurbine(EnergySource):
    def calculate_annual_energy_output(self, k=150):
        return self.height * self.windspeedaverage * k

    def calculate_resource_depletion_rate(self, k=1000):
        if self.height <= 0 or self.windspeedaverage <= 0:
            raise ResourceDepletionRateCalculateError
        return k / (self.height * self.windspeedaverage)


class HydroPlant(EnergySource):
    def calculate_annual_energy_output(self, k=12):
        return self.flowrate * self.drop * k

    def calculate_resource_depletion_rate(self):
        if self.drop <= 0:
            raise ResourceDepletionRateCalculateError
        return self.flowrate / self.drop


class OffshoreWindTurbine(EnergySource):
    def calculate_annual_energy_output(self, k=160):
        return self.height * self.windspeedaverage * (1 - self.corrosionfactor) * k

    def calculate_resource_depletion_rate(self, k=1200):
        if self.height  <= 0 or self.windspeedaverage <= 0 or (1 - self.corrosionfactor) <= 0:
            raise ResourceDepletionRateCalculateError
        return k / (self.height * self.windspeedaverage * (1 - self.corrosionfactor))
