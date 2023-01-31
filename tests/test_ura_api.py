import unittest
from ura_api import ura_api

ACCESS_KEY = '<Your access key here>'

class TestURAAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.ura = ura_api.ura_api(ACCESS_KEY)

    def tearDown(self):
        pass    

    ## Car Parks
    def test_car_pack_available_lots(self):
        self.assertIsNotNone(self.ura.car_pack_available_lots())

    def test_car_pack_list_and_rates(self):
        self.assertIsNotNone(self.ura.car_pack_list_and_rates())

    def test_season_car_pack_list_and_rates(self):
        self.assertIsNotNone(self.ura.season_car_pack_list_and_rates())


    ## Private Properties
    def test_private_residential_property_transactions(self):
        self.assertIsNotNone(self.ura.private_residential_property_transactions())

    def test_private_non_landed_residential_properties_median_rentals_by_name(self):
        self.assertIsNotNone(self.ura.private_non_landed_residential_properties_median_rentals_by_name())

    def test_private_residential_properties_rental_contract(self):
        self.assertIsNotNone(self.ura.private_residential_properties_rental_contract('14q1'))

    def test_private_residential_property_units_sold_by_developers(self):
        self.assertIsNotNone(self.ura.private_residential_property_units_sold_by_developers('0919'))

    def test_private_residential_projects_in_the_pipeline(self):
        self.assertIsNotNone(self.ura.private_residential_projects_in_the_pipeline())


    ## Planning Decisions
    def test_planning_decisions(self):
        self.assertFalse(self.ura.planning_decisions())
        self.assertFalse(self.ura.planning_decisions(year=1945))
        self.assertIsNotNone(self.ura.planning_decisions(year=2018))
        self.assertIsNotNone(self.ura.planning_decisions(last_dnload_date='01/01/2018'))


    ## Approved Use
    def test_approved_residential_use(self):
        self.assertIsNotNone(self.ura.approved_residential_use(6, 'Petir%20Road'))
        self.assertIsNotNone(self.ura.approved_residential_use('6', 'Petir%20Road', '5', '5'))
        pass

if __name__ == '__main__':
    unittest.main()
