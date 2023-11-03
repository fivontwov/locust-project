# run test-project
-  create database named blogapi
-  import blogapi.sql
-  modify information in application.properties into your setting:
spring.datasource.username= root
spring.datasource.password=

# run locust to test
-  Post signin user
POST http://localhost:8080/api/auth/signin
{
	"usernameOrEmail": "leanne",
	"password": "password"
}

-  run in httpsClass.py in pyCharmProject by command line:
locust -f httpsClass.py
-  open locust interface to test in http://localhost:8089/. You can choose Number of users, Spawn rate.
Host will have in default


