from locust import task, between
from locust.contrib.fasthttp import FastHttpUser


class WebsiteUser(FastHttpUser):
    wait_time = between(5, 9)

    @task
    def index(self):
        self.client.get('/')
