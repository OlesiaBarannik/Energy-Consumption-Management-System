import unittest
import energy_source

class EnergySourceTest(unittest.TestCase):

    def test_solarpanel(self):
        solarpanel = energy_source.SolarPanel(area=20, efficiency=15)

        annual_energy_output_expected_result = 4500
        self.assertEqual(solarpanel.calculate_annual_energy_output(), annual_energy_output_expected_result)

        resource_depletion_rate_expected_result = 6.67
        self.assertEqual(round(solarpanel.calculate_resource_depletion_rate(), 2), resource_depletion_rate_expected_result)

    def test_windturbine(self):
        windturbine = energy_source.WindTurbine(height=50, windspeedaverage=6)

        annual_energy_output_expected_result = 45000
        self.assertEqual(windturbine.calculate_annual_energy_output(), annual_energy_output_expected_result)

        resource_depletion_rate_expected_result = 3.33
        self.assertEqual(round(windturbine.calculate_resource_depletion_rate(), 2), resource_depletion_rate_expected_result)

    def test_hydroplant(self):
        hydroplant = energy_source.HydroPlant(flowrate=300, drop=20)

        annual_energy_output_expected_result = 72000
        self.assertEqual(hydroplant.calculate_annual_energy_output(), annual_energy_output_expected_result)

        resource_depletion_rate_expected_result = 15
        self.assertEqual(round(hydroplant.calculate_resource_depletion_rate(), 2), resource_depletion_rate_expected_result)

    def test_offshorewindturbine(self):
        offshorewindturbine = energy_source.OffshoreWindTurbine(height=70, windspeedaverage=8, corrosionfactor=0.2)

        annual_energy_output_expected_result = 71680
        self.assertEqual(offshorewindturbine.calculate_annual_energy_output(), annual_energy_output_expected_result)

        resource_depletion_rate_expected_result = 2.68
        self.assertEqual(round(offshorewindturbine.calculate_resource_depletion_rate(), 2), resource_depletion_rate_expected_result)

    def test_invalid_data_types(self):
        with self.assertRaises(TypeError):
            solarpanel = energy_source.SolarPanel(area="twenty", efficiency=15)
            solarpanel.validate()

        with self.assertRaises(TypeError):
            windturbine = energy_source.WindTurbine(height=50, windspeedaverage="six")
            windturbine.validate()

        with self.assertRaises(TypeError):
            hydroplant = energy_source.HydroPlant(flowrate=300, drop="twenty")
            hydroplant.validate()

        with self.assertRaises(TypeError):
            offshorewindturbine = energy_source.OffshoreWindTurbine(height=70, windspeedaverage="eight", corrosionfactor=0.2)
            offshorewindturbine.validate()

    def test_calculate_resource_depletion_rate_offshorewindturbine(self):
        with self.assertRaises(energy_source.ResourceDepletionRateCalculateError):
            error_resource_depletion_rate = energy_source.OffshoreWindTurbine(height=0, windspeedaverage=8, corrosionfactor=0.2)
            error_resource_depletion_rate.calculate_resource_depletion_rate()

    def test_calculate_resource_depletion_rate_solarpanel(self):
        with self.assertRaises(energy_source.ResourceDepletionRateCalculateError):
            error_solarpanel = energy_source.SolarPanel(area=20, efficiency=0)
            error_solarpanel.calculate_resource_depletion_rate()

    def test_calculate_resource_depletion_rate_windturbine(self):
        with self.assertRaises(energy_source.ResourceDepletionRateCalculateError):
            error_windturbinel = energy_source.WindTurbine(height=0, windspeedaverage=6)
            error_windturbinel.calculate_resource_depletion_rate()

    def test_calculate_resource_depletion_rate_hydroplant(self):
        with self.assertRaises(energy_source.ResourceDepletionRateCalculateError):
            error_hydroplant = energy_source.HydroPlant(flowrate=300, drop=0)
            error_hydroplant.calculate_resource_depletion_rate()

