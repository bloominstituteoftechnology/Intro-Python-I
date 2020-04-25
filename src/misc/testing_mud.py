
curl - X POST - H "Content-Type: application/json" - d '{"username":"heather4", "password1":"testpassword4", "password2":"testpassword4"}' https: // lambda-mud-test.herokuapp.com/api/registration/

curl - X POST - H "Content-Type: application/json" - d '{"username":"heather4", "password":"testpassword4"}' https: // lambda-mud-test.herokuapp.com/api/login/

curl - X GET - H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' https: // lambda-mud-test.herokuapp.com/api/adv/init/

curl - X POST - H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' - H "Content-Type: application/json" - d '{"direction":"n"}' https: // lambda-mud-test.herokuapp.com/api/adv/move/

curl - X POST - H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' - H "Content-Type: application/json" - d '{"message":"Hello, world!"}' https: // lambda-mud-test.herokuapp.com/api/adv/say/

'''
curl -X POST -H "Content-Type: application/json" -d '{"username":"heather4", "password1":"testpassword4", "password2":"testpassword4"}' https://lambda-mud-test.herokuapp.com/api/registration/

curl -X POST -H "Content-Type: application/json" -d '{"username":"heather4", "password":"testpassword4"}' https://lambda-mud-test.herokuapp.com/api/login/

curl -X GET -H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' https://lambda-mud-test.herokuapp.com/api/adv/init/

curl -X POST -H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-mud-test.herokuapp.com/api/adv/move/

curl -X POST -H 'Authorization: Token 00486675b0efa8062a30ac77c5f0c169ff8fde76' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' https://lambda-mud-test.herokuapp.com/api/adv/say/
'''
