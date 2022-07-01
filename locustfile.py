from locust import HttpUser, task, between

import random

class ReviewsAPI(HttpUser):
    wait_time = between(1, 2)
    @task
    # def test(self):
    #     self.client.get("/test")
    def reviews(self):
        id = random.randint(1, 950000)
        self.client.get(f"/reviews?product_id={id}")
    