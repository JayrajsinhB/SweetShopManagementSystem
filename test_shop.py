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
        
    def delete_sweet(self):
        shop = SweetShop()
        
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
    
        shop.delete_sweet("1001")
        result = shop.get_all_sweets()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "1002")

        
if __name__ == '__main__':
    unittest.main()