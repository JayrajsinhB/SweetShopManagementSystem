import unittest
from shop import SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        
        # add_sweet(id, name, category, price, quantity)
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        
        result = shop.get_all_sweets()
        self.assertEqual(len(result), 1)
        
        
        sweet = result[0]  # first sweet in list
        self.assertEqual(sweet["id"], "1001")
        self.assertEqual(sweet["name"], "Kaju Katli")
        self.assertEqual(sweet["category"], "Nut-Based")
        self.assertEqual(sweet["price"], 50)
        self.assertEqual(sweet["quantity"], 20)

        
if __name__ == '__main__':
    unittest.main()