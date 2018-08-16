import time
from concurrent import futures

import grpc
import src.authentification_pb2
import src.authentification_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Auth(src.authentification_pb2_grpc.AuthServiceServicer):

    def SignIn(self, request, context):

        print("SignIn incoming value: " + request.username)
        res = False

        if request.username == "test" :
            res = True

        print("SignIn return value: " + str(res))

        # isSuccess - field in .proto (message Response), must be same
        return src.authentification_pb2.Response(isSuccess = res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    src.authentification_pb2_grpc.add_AuthServiceServicer_to_server(Auth(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()

