from locust import HttpLocust, TaskSet, task, between

class MyTaskSet(TaskSet):

    @task
    def loadtest(self):
        response1 = self.client.get("/get_token")
        token = response1.json()["uuid"]
        print (token)

        response2 = self.client.post("/post_token", {"token": token})
        print (response2.json()["body"])

class LoadTest(HttpLocust):
    task_set = MyTaskSet
