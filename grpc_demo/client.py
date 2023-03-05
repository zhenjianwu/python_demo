import time

import grpc

from grpc_demo import test_pb2_grpc, test_pb2


def one_req_one_resp_cli():
    response = stub.OneReqOneResp(test_pb2.Req(cmd="test", params=""))
    print("Greeter client received: code->" + str(response.code) + " msg->" + response.msg + " data:" + response.data)


def one_req_multi_resp_cli():
    response = stub.OneReqMultiResp(test_pb2.Req(cmd="test", params=""))
    for item in response:
        print("code->" + str(item.code) + " msg->" + item.msg + " data:" + item.data)


def multi_req_one_resp_cli():
    def req_multi():
        for i in range(10):
            time.sleep(1)
            yield test_pb2.Req(cmd="test", params="")

    resp = stub.MultiReqOneResp(req_multi())
    print("code->" + str(resp.code) + " msg->" + resp.msg + " data:" + resp.data)


def multi_req_multi_resp_cli():
    def req_multi():
        for i in range(10):
            time.sleep(1)
            yield test_pb2.Req(cmd="test", params="")

    response = stub.MultiReqMultiResp(req_multi())
    for item in response:
        print("code->" + str(item.code) + " msg->" + item.msg + " data:" + item.data)


if __name__ == '__main__':
    # 本次不使用SSL，所以channel是不安全的
    channel = grpc.insecure_channel('localhost:50051')
    # 客户端实例
    stub = test_pb2_grpc.TestSrvStub(channel)
    # one_req_one_resp_cli()
    # one_req_multi_resp_cli()
    # multi_req_one_resp_cli()
    multi_req_multi_resp_cli()

