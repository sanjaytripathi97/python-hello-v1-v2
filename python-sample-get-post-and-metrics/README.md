CURL REQUEST:-

$ curl -kv -H "Expect: 100-continue" REPLACE-URL-HERE --request POST -H 'Content-Type: appication/json' --data '{"code": 0}'


for checking metrics :-
$ curl http://<url:8001>/python-metrics
