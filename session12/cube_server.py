"""Session 12 exercise: simple gRPC cube server (requires generated code)."""
from concurrent import futures
import grpc

try:
    import cube_pb2
    import cube_pb2_grpc
except Exception:  # pragma: no cover - generation step required
    cube_pb2 = None
    cube_pb2_grpc = None

class CubeServicer:
    def Cube(self, request, context):
        return cube_pb2.CubeReply(result=request.number ** 3)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    if cube_pb2_grpc:
        cube_pb2_grpc.add_CubeServiceServicer_to_server(CubeServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("Generate gRPC code with grpc_tools.protoc then run this server.")
