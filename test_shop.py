import unittest
from shop import SweetShop
class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        # shop.add_sweet("ID", "Name", "Category", "Price ", "Quantity")
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", "50 ", "20")
        self.assertEqual(shop.sweets["1001"]["Name"], "Kaju Katli")
        
        result = shop.get_all_sweets()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0],["name"], "Kaju Katli")
        
if __name__ == '__main__':
    unittest.main()