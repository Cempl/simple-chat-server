from concurrent import futures

import grpc
import src.authentification_pb2
import src.authentification_pb2_grpc


class Auth(src.authentification_pb2_grpc.AuthServiceServicer):

    def SignIn(self, request, context):

        res = False

        if request == "test" :
            res = True

        return src.authentification_pb2.Response(res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    src.authentification_pb2_grpc.add_AuthServiceServicer_to_server(Auth(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


def main():
    serve()


if __name__ == "__main__":
    main()