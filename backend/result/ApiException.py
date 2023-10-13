def getApiException(error):
    self = ApiException(error['errorCode'], error['httpCode'], error['desc'])
    return self


class ApiException(RuntimeError):
    errorCode = 0
    httpCode = 0
    desc = ''

    def __init__(self, errorCode, httpCode, desc):
        self.errorCode = errorCode
        self.httpCode = httpCode
        self.desc = desc
