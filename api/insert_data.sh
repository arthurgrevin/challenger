#
# insert 3 challenges
#
curl http://localhost:5000/challenges/ -H "Content-Type: application/json" -d '{"title": "My first challenge", "nb_days":3, "start_date":"2017-01-23", "end_date":"2017-01-26"}' -X POST
curl http://localhost:5000/challenges/ -H "Content-Type: application/json" -d '{"title": "My second challenge", "nb_days":3, "start_date":"2017-01-23", "end_date":"2017-01-26"}' -X POST
curl http://localhost:5000/challenges/ -H "Content-Type: application/json" -d '{"title": "My third challenge", "nb_days":3, "start_date":"2017-01-23", "end_date":"2017-01-26"}' -X POST
#
# get all challenges
# curl http://localhost:5000/challenges/
#
# get a challenge
# curl http://localhost:5000/challenges/1
#
# delete a challenge
# curl http://localhost:5000/challenges/1 -X DELETE
# 
# update a challenge
# curl http://localhost:5000/challenges/2 -H "Content-Type: application/json" -d '{"title": "My 2nd challenge", "nb_days":3, "start_date":"2017-01-23", "end_date":"2017-01-26"}' -X PUT
#
# get days of a challenge
# curl http://localhost:5000/challenges/1/days/