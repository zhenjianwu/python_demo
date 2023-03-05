import logging
import time
from concurrent import futures

import grpc

from grpc_demo import test_pb2_grpc, test_pb2


class TestServicer(test_pb2_grpc.TestSrvServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.time_sleep = 3

    def OneReqOneResp(self, request, context):
        print("简单的RPC")
        print("收到数据 cmd: " + request.cmd + " params: " + request.params)
        return test_pb2.MsgBatch(code=0, msg="success", data="")

    def OneReqMultiResp(self, request, context):
        print("OneReqMultiResp")
        for i in range(10):
            time.sleep(100)
            yield test_pb2.MsgBatch(code=0, msg="success", data="OneReqMultiResp" + str(i))

    def MultiReqOneResp(self, request_iterator, context):
        print("MultiReqOneResp")
        for request in request_iterator:
            print("收到数据 cmd: " + request.cmd + " params: " + request.params)

        return test_pb2.MsgBatch(code=0, msg="success", data="")

    def MultiReqMultiResp(self, request_iterator, context):
        print("MultiReqMultiResp")
        for request in request_iterator:
            print("收到数据 cmd: " + request.cmd + " params: " + request.params)
            yield test_pb2.MsgBatch(code=0, msg="success", data="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))  # 以多线程的方式监听
    test_pb2_grpc.add_TestSrvServicer_to_server(TestServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
