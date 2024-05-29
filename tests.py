import unittest
import energy_source

class EnergySourceTest(unittest.TestCase):
    def test_solarpanel(self):
        solarpanel = energy_source.SolarPanel(area=20, efficiency=15)
        expected_result = 4500
        self.assertEqual(solarpanel.get_result(), expected_result)

    def test_windturbine(self):
        windturbine = energy_source.WindTurbine(height=50, windspeedaverage=6)
        expected_result = 45000
        self.assertEqual(windturbine.get_result(), expected_result)

    def test_hydroplant(self):
        hydroplant = energy_source.HydroPlant(flowrate=300, drop=20)
        expected_result = 72000
        self.assertEqual(hydroplant.get_result(), expected_result)

    def test_offshorewindturbine(self):
        offshorewindturbine = energy_source.OffshoreWindTurbine(height=70, windspeedaverage=8, corrosionfactor=0.2)
        expected_result = 71680
        self.assertEqual(offshorewindturbine.get_result(), expected_result)