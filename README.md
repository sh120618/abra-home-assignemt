# abra-home-assignemt
Djano REST API Python backend

Working server:
https://abra-home-assignemnt.herokuapp.com/

To register:
https://abra-home-assignemnt.herokuapp.com/auth/users/

To log in use following:
1. goto: https://abra-home-assignemnt.herokuapp.com/auth/jwt/create
2. insert username and password
3. AccessToken available for 1 day, can't submit requests with postman and authorization. 
4. Can check auth using Chrome extension: MODChrome, add "Authorization" field +  "JWT" + "<access_token>"

https://abra-home-assignment/messeages -> 
view all messages as a receiver or as a sender of the logged in user.

http://127.0.0.1:8000/messeages/{:id} ->
going to message details, mark message as read, allow to delete the message

https://abra-home-assignment/messeages/unread ->
all unread messages were sent to the logged in user

