class SweetShop:
    
    def __init__(self):
        self.sweets = []
        
    # Add Sweets
    def add_sweet(self, id, name, category, price, quantity):
        sweet = {
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        self.sweets.append(sweet)
        
    def delete_sweet(self, id):
        for sweet in self.sweets:
            if sweet["id"] == id:
                self.sweets.remove(sweet)
                return True
        return False

        
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

    def update_sweet(self, id, name = None, category = None, price = None, quantity = None):
        for sweet in self.sweets:
            if sweet['id'] == id:
                if name is not None:
                    sweet["name"] = name
                if category is not None:
                    sweet["category"] = category
                if price is not None:
                    sweet["price"] = int(price)
                if quantity is not None:
                    sweet["quantity"] = int(quantity)
                
                return True
            
        return False

                
        
    def get_all_sweets(self):
        return self.sweets