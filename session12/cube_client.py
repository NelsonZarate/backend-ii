"""Session 12 exercise: simple gRPC cube client (requires generated code)."""
import grpc

try:
    import cube_pb2
    import cube_pb2_grpc
except Exception:
    cube_pb2 = None
    cube_pb2_grpc = None

def run(number: int):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = cube_pb2_grpc.CubeServiceStub(channel)
        req = cube_pb2.CubeRequest(number=number)
        resp = stub.Cube(req)
        return resp.result

if __name__ == "__main__":
    print("Run after generating code and starting server. Example: run(3)")
