from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(1, 2.5) 
    
    @task
    def my_task(self):
        self.client.get("/questions/1/category/") # 엔드포인트작성