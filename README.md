# grpc_suburi

gRPCの素振り

docker で動くようになったように見える。

# build

```txt
docker build --file="./build/Dockerfile" . -t grpc-suburi
```

# run

```txt
docker run -d -p 8080:50051 grpc-suburi:latest
```

# テスト

```txt
grpcurl -plaintext -d '{"name": "Java"}' 172.17.0.1:8080 konpeko.Pekora.IdolGreeting
```
