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
        results = self.sweets

        if name:
            results = [s for s in results if name.lower() in s["name"].lower()]

        return results
        
    def get_all_sweets(self):
        return self.sweets