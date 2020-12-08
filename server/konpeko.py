from concurrent import futures
import logging

import grpc

import konpeko_pb2
import konpeko_pb2_grpc


class Pekora(konpeko_pb2_grpc.PekoraServicer):
    def IdolGreeting(self, request, context):
        return konpeko_pb2.GreetReply(message="%s さん、こんぺこ～！" % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    konpeko_pb2_grpc.add_PekoraServicer_to_server(Pekora(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
