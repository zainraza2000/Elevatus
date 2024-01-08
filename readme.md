fastAPI using repository pattern
setup:
docker-compose up

steps:

- create user
- get token through the /token endpoint, pass the email in the body
- use that token as "Api_key" in headers to authorize as a user
- can test through swagger "localhost:8000/docs"
