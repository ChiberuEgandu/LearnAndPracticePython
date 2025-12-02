import unittest
from car import Car

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Camry", year=2020, price=20000.0)

    # 1. assertEqual(a, b) → a == b
    def test_car_make_and_model(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.year, 2020)
        self.assertEqual(self.car.price, 20000.0)
        

        

    # 2. assertNotEqual(a, b) → a != b 
    def test_model_is_not_different(self):
        self.assertNotEqual(car.make, "Toyota")
        self.assertNotEqual(car.model, "Camry")
        self.assertNotEqual(car.year, 2020)
        self.assertNotEqual(car.price, 20000.0)

    # 3. assertTrue(x) → bool(x) is True
    def test_car_starts(self):
        self.assertTrue(car.make, "Honda")

    # 4. assertFalse(x) → bool(x) is False
    def test_car_stops(self):
        pass    

    # 5. assertIs(a, b) → a is b
    def test_same_object_reference(self):
        pass    

    # 6. assertIsNone(x) → x is None
    def test_owner_initially_none(self):
        pass    

    # 7. assertIn(a, b) → a in b
    def test_feature_added_to_list(self):
        pass    

    # 8. assertIsInstance(a, b) → isinstance(a, b)
    def test_car_is_instance_of_car_class(self):
        pass    

    # 9. assertAlmostEqual(a, b) → floating-point comparison
    def test_price_with_tax_calculation(self):
        pass    

    # 10. assertGreater(a, b) → a > b
    def test_increase_price(self):
        pass    
    # 11. assertLess(a, b) → a < b
    def test_car_year_less_than_future_year(self):
        pass

if __name__ == '__main__':
    unittest.main()