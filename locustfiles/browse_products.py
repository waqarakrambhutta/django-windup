from locust import HttpUser,task,between
from random import randint

# to run this file we use the command loscust -f locustfiles/browse_products.py

class WebsiteUser(HttpUser):
    wait_time= between(1,5) # it means it each task takes 1 to 5 seconds to excecute.


    @task(2) # 2 means wait of 2.
    def view_products(self):

        print('Viewing Products.')

        collection_id  = randint(2,6)
        self.client.get(f'/store/products/?collection_id={collection_id}',
        name='/store/products'                 
        )


    @task(4)
    def view_product(self):

        print('Viewing product detail.')

        product_id = randint(1,1000)
        self.client.get(
            f'/store/products/{product_id}',
            name='/store/products/:id'
        )


    @task(1)
    def add_to_cart(self):
        print('Adding product to carts.')
        product_id = randint(1,10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name = 'store/carts/items',
            json={'product_id':product_id,'quantity': 1}
        )  


    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']