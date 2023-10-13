from enum import Enum


class errors(Enum):
    UNKNOWN_ERROR = {'errorCode': 1, 'httpCode': 500, 'desc': 'Server unknown error'}

    # ------------------ 1xx: Login, Authorized ------------------

    # UNAUTHORIZED = {'errorCode': 100, 'httpCode': 401, 'desc': 'Unauthorized'}
    # FORBIDDEN = {'errorCode': 101, 'httpCode': 403, 'desc': "Forbidden"}
    # WRONG_PASSWORD = {'errorCode': 102, 'httpCode': 403, 'desc': 'Wrong user or password'}
    #
    # PERMISSION_DENIED = {'errorCode': 103, 'httpCode': 403, 'desc': "Permission denied"}
    # INVALID_CSRF_TOKEN = {'errorCode': 104, 'httpCode': 403, 'desc': "Invalid csrf token"}
    # INVALID_ID = {'errorCode': 105, 'httpCode': 400, 'desc': "Invalid id"}
    # INVALID_PASSWORD = {'errorCode': 106, 'httpCode': 400, 'desc': "Invalid password"}
    # USER_ALREADY_EXIST = {'errorCode': 107, 'httpCode': 409, 'desc': "User already exist"}
    # ROOM_ALREADY_EXIST = {'errorCode': 107, 'httpCode': 409, 'desc': "Room already exist"}
    # WRONG_ROOM_ID = {'errorCode': 108, 'httpCode': 403, 'desc': 'This room is not exist'}

    # ------------------ 3xx: Bad Request ------------------------
    # BAD_REQUEST = {'errorCode': 300, 'httpCode': 400, 'desc': "Bad request"}
    # UNSUPPORTED_METHOD = {'errorCode': 301, 'httpCode': 405, 'desc': "Unsupported method"}
    # INVALID_DATA_FORMAT = {'errorCode': 302, 'httpCode': 400, 'desc': "Invalid data format"}
    # INVALID_NAME = {'errorCode': 305, 'httpCode': 400, 'desc': "Invalid name"}
    # NOT_A_MULTIPART_REQUEST = {'errorCode': 306, 'httpCode': 400, 'desc': "Not a multipart request"}

    # ------------------ 4xx: Other -------------------
    # DATA_UPLOAD_FAILED = {400, 400, "Data upload failed"}

    # ------------------ 5xx: Generate Error ------------
