from concurrent import futures
import grpc
import greeter_pb2
import greeter_pb2_grpc

class Greeter(greeter_pb2_grpc.GreeterServicer):

    def __init__(self):
        self.counter = 0

    def Count(self):
        self.counter += 1
        return self.counter

    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(
            message=f"Hello, {request.name}! counter = {self.Count()}"
        )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()