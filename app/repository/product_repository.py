class ProductRepository:
    def __init__(self):
        self.products = []
        self.id_counter = 1

    def save(self, product):
        product['id'] = self.id_counter
        self.products.append(product)
        self.id_counter += 1
        return product

    def get_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None
