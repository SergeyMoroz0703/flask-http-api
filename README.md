# flask-mongoDB-http-api

Here provided easy HTTP API wich support GET, POST method requests. I'm going to added another methods later. <br>
API works with Mongo database, namely with `users_db` <br>

----
Example of GET request for one user: <br> `localhost:5000/users?name=James&surname=Bond&online=false` or <br>
`requests.get(url='localhost:5000', params={"name": "James", "surname": "Bond", "online": "False"})` <br>
To get all users from database just send GET request with payload {}. <br>

Example of POST request for add user to database: <br>
`user = {"name": "James", "surname": "Bond", "online": "False"}` <br>
`requests.post(url='localhost:5000', data=json.dumps(user), headeds={"Content-Type": "application/json"}`

----
