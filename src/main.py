from fastapi import FastAPI
from .database import db
from .models import basemodel
from .routers import jobs, auth
from fastapi.exceptions import RequestValidationError
from .middlewares.error_handlers import validation_exception_handler,integrity_error_handler
from sqlalchemy.exc import IntegrityError

basemodel.Base.metadata.create_all(bind=db.engine)

app = FastAPI()



#exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
#integrity error handler
app.add_exception_handler(IntegrityError, integrity_error_handler)


app.include_router(jobs.router)
app.include_router(auth.router)

@app.get("/")   
def read_root():
    return {"Hello": "This is the root of the API"}