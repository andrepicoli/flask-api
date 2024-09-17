from app.repository.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, data):
        product = {
            'name': data.get('name'),
            'price': data.get('price'),
            'description': data.get('description')
        }
        return self.repository.save(product)

    def get_product_by_id(self, product_id):
        return self.repository.get_by_id(product_id)
