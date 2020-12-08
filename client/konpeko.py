from __future__ import print_function
import logging

import grpc

import konpeko_pb2
import konpeko_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = konpeko_pb2_grpc.PekoraStub(channel)
        response = stub.IdolGreeting(konpeko_pb2.GreetRequest(name="yumechi"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
