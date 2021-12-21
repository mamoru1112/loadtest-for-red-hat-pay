from locust import HttpLocust, TaskSet, task, constant

class MyTaskSet(TaskSet):

    @task
    def loadtest(self):
        response1 = self.client.post("/pay/1")
        token = response1.json()["tokenId"]["value"]
        print (token)

        response2 = self.client.request(method="POST", url="/pay/1/" + token + "/1/1")
        print (response2.json())

class LoadTest(HttpLocust):
    task_set = MyTaskSet
    wait_time = constant(1)
