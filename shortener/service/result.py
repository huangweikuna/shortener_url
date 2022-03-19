import logging
import traceback

from django.http import JsonResponse


class HttpCode(object):
    ok = 0
    client_error = 400
    server_error = 500


# 定义统一的 json 字符串返回格式
def result(code=HttpCode.ok, message="", data=None):
    json_dict = {"code": code, "message": message, "data": data}
    return JsonResponse(json_dict)


def ok(data=None):
    return result(message="success", data=data)


def client_error(message, code=HttpCode.client_error):
    return result(code=code, message=message)


def server_error(message, code=HttpCode.server_error):
    return result(code=code, message=message)
