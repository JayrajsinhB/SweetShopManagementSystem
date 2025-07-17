class SweetShop:
    
    def __init__(self):
        self.sweets = []
        
    # add sweet method
    def add_sweet(self, id, name, category, price, quantity):
        sweet = {
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        self.sweets.append(sweet)
        
    def search_sweets(self, name=None, category=None, price_range=None):
        results = []

        for sweet in self.sweets:
            match = True

            if name and name.lower() not in sweet["name"].lower():
                match = False

            if category and category.lower() != sweet["category"].lower():
                match = False

            if price_range:
                min_price, max_price = price_range
                if not (min_price <= sweet["price"] <= max_price):
                    match = False

            if match:
                results.append(sweet)

        return results


        
    def get_all_sweets(self):
        return self.sweets