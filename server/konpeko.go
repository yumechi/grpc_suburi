// Package main implements a server for Greeter service.
package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "github.com/yumechi/grpc_suburi/server/protos"
)

const (
	port = ":50051"
)

// server is used to implement helloworld.GreeterServer.
type server struct {
	pb.UnimplementedPekoraServer
}

// SayHello implements helloworld.GreeterServer
func (s *server) IdolGreeting(ctx context.Context, in *pb.GreetRequest) (*pb.GreetReply, error) {
	log.Printf("Received: %v", in.GetName())
	return &pb.GreetReply{Message: in.GetName() + "さん、こんぺこ～！"}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterPekoraServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}