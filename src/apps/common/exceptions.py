from rest_framework.exceptions import APIException


class CustomException(APIException):
    status_code = 400
    default_detail = ""
    default_code = ""
