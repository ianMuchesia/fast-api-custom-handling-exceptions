from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from sqlalchemy.exc import IntegrityError
from ..errors.notauthorized import NotAuthorized


#this is the error handler for validation errors 
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detail = exc.errors()
    # print(detail)
    # print(detail[0]['loc'][1])
    # print(detail[0]['type'])
    try:
        
        if detail[0]['loc'][1] == 'token':        
            return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"msg":"Not authenticated"},
        )
        elif detail[0]['type'] == 'missing':
            return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"msg":"Missing required fields"},
        )
    except:
        return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"msg":detail[0]['msg']},
        )


#no use for this yet
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg": exc.detail},
    )


#no idea what this is for
async def starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg": exc.detail},
    )


#this is the error handler for database integrity errors
async def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=500,  # Internal Server Error
        content={"msg": "Database Integrity Error"},
    )