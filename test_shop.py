import unittest
from shop import SweetShop

class TestSweetShop(unittest.TestCase):
    
    # add sweet function
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
        
    def test_delete_sweet(self):
        shop = SweetShop()
        
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
    
        shop.delete_sweet("1001")
        result = shop.get_all_sweets()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "1002")
        
    def test_search_sweets_by_name(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Gajar Halwa", "Vegetable-Based", 40, 5)

        results = shop.search_sweets(name="Gulab")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "1002")
        
    def test_search_sweets_by_category(self):
        shop = SweetShop()
        
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 25, 15)
        
        results = shop.search_sweets(category = "Milk-Based")
        
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "Gulab Jamun")
        self.assertEqual(results[1]["name"], "Rasgulla")
        
    def test_search_sweets_by_price_range(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)
        
        results = shop.search_sweets(price_range = (40, 60))
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Kaju Katli")
        
    def test_sort_sweets_by_id(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)
        
        sorted_sweets = shop.sort_sweets(by = "id")
        ids = [sweet["id"] for sweet in sorted_sweets]
        self.assertEqual(ids, ["1001", "1002", "1003"])

    def test_sort_sweets_by_name(self):
        shop = SweetShop()
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)

        sorted_sweets = shop.sort_sweets(by="name")
        names = [sweet["name"] for sweet in sorted_sweets]
        self.assertEqual(names, ["Gulab Jamun", "Kaju Katli", "Rasgulla"])
        
    def test_sort_sweets_by_category(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)

        sorted_sweets = shop.sort_sweets(by="category")
        categories = [sweet["category"] for sweet in sorted_sweets]
        self.assertEqual(categories, ["Milk-Based", "Milk-Based", "Nut-Based"])

    def test_sort_sweets_by_price(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)

        sorted_sweets = shop.sort_sweets(by="price")
        prices = [sweet["price"] for sweet in sorted_sweets]
        self.assertEqual(prices, [30, 50, 70])
        
    def test_sort_sweets_by_quantity(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)

        sorted_sweets = shop.sort_sweets(by="quantity")
        quantities = [sweet["quantity"] for sweet in sorted_sweets]
        self.assertEqual(quantities, [10, 15, 20])
    
    def test_update_sweet(self):
        shop = SweetShop()
        shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
        shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
        shop.add_sweet("1003", "Rasgulla", "Milk-Based", 70, 15)
        
        shop.update_sweet("1001", name= "Kaju Katli", price = "70")
        
        result = shop.get_all_sweets()
        self.assertEqual(result[0]["name"], "Kaju Katli")
        self.assertEqual(result[0]["price"], 70)
        self.assertEqual(result[0]["quantity"], 20)  # unchanged
    
if __name__ == '__main__':
    unittest.main()