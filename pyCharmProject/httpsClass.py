from locust import HttpUser, task, between
class myScript(HttpUser):
    wait_time = between(1,2)
    host = 'http://localhost:8080/api/auth'
    @task
    def login(self):
        res=self.client.post('/signin', json={"usernameOrEmail": "leanne",
                                                       "password": "password"},name='login')

    @task
    def logout(self):
        res=self.client.post('/signOut', json={"usernameOrEmail": "leanne",
                                                       "password": "password"},name='logout')


    @task
    def profile(self):
        res=self.client.get('/profile',name='get profile')

    @task
    def signup(self):
        res=self.client.get('/all',name='get all')

