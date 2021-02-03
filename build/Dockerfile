FROM golang:1.15-alpine3.13 as build

WORKDIR /go/app

COPY . .

RUN ls
RUN go build konpeko/server/server_main.go

FROM alpine:3.13

WORKDIR /app

COPY --from=build /go/app/server_main .

RUN set -x && \
  addgroup go && \
  adduser -D -G go go && \
  chown -R go:go /app/server_main

CMD ["./server_main"]
