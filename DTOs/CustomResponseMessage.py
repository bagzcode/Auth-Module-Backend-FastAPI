import json


class CustomResponseMessage:
    def __call__(self, status_code=None, message=None):
        return {
            "status_code": status_code,
            "message": message
        }
