# Docker Overlord

Technologies:
- AWS
- Docker
- Python FastAPI
- Vue JS

## Environment

Create `.env` with:
```
JWT_SIGNING_TOKEN=abc...xyz
GITHUB_CLIENT_ID=abc...xyz
GITHUB_CLIENT_SECRET=abc...xyz
AWS_DEFAULT_REGION=ap-southeast-1
AWS_ACCESS_KEY_ID=ABC...XYZ
AWS_SECRET_ACCESS_KEY=abc...xyz
```

No need for AWS secrets if using EC2 roles.

docker exec -it app sqlite3 /data/sqlite.db ".read schema.sql"
docker exec -it app sqlite3 /data/sqlite.db "UPDATE users SET admin = 1"

## Production

```
docker run \
  --name app -d \
  --restart=unless-stopped \
  -p 5000:80 \
  -v /data:/data \
  --env-file /data/.env \
  wfong/docker-overlord:c5d89c6be5a997ccdd8f5a96055e8ab1e5f57b11
```

## Development

```
docker stop app
docker build -t docker-overlord .
docker run \
  --name app --rm -d \
  -p 5000:80 \
  -v ${PWD}/vue:/vue \
  -v ${PWD}/data:/data \
  --env-file .env \
  docker-overlord
docker logs app -f
```
