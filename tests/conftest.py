

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/jobs"



from fastapi.testclient import TestClient
from src.main import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.basemodel import Base
from src.database.db import get_db


engine = create_engine(SQLALCHEMY_DATABASE_URL)

Testing_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)










@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = Testing_SessionLocal()
    try:
        yield db
    finally:
        db.close()




@pytest.fixture()
def client(session):
    def override_get_db():
 
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)



@pytest.fixture
def test_user(client):
    user_data = {
        "username":"modoki",
        "email":"msodoki@email.com",
        "password":"password"
    }
    
    res = client.post("/auth/register", json=user_data)
    
    assert res.status_code == 201
    # return UserResponse(**res.json())
    return user_data