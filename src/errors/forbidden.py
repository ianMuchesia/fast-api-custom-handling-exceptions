# errors/notfound.py
from fastapi import HTTPException, status

class  ForbiddenError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
