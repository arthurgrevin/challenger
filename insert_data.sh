curl http://localhost:5000/challenges/ -d "id=ch1" -d "title=My first challenge" -X PUT
curl http://localhost:5000/challenges/ -d "id=ch2" -d "title=My second challenge" -X PUT

curl http://localhost:5000/challenges/ -d '{"id:ch3", "title": "My third challenge"}' -X PUT