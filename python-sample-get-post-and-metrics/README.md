CURL REQUEST:-

$ curl -kv -H "Expect: 100-continue" REPLACE-URL-HERE --request POST -H 'Content-Type: appication/json' --data '{"code": 0}'


for checking metrics :-
$ curl http://<url:8001>/python-metrics


![image](https://github.com/user-attachments/assets/194e1f08-8a47-4438-85f7-94d2298e1ec1)
