from fastapi.testclient import TestClient
from src.main import app
import pytest
import uuid
from src.schemas.user_schemas import UserResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.basemodel import Base,User,Job
from src.database.db import get_db
from src.utils.ouath2 import create_access_token

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/jobs"



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
   
    return res.json()
   


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user["id"], "user_email":test_user["email"]})
    
    
@pytest.fixture
def authorized_client(client, token):
    client.headers["Authorization"] = f"Bearer {token}"
    return client


@pytest.fixture
def test_jobs(test_user, session):
    posts_data =[
        {
            "id": str(uuid.uuid4()),
            "title":"Job 1",
            "description":"Job 1 description",
            "location":"Job 1 location",
            "company":"Job 1 company",
            "company_url":"Job 1 company_url",
            "is_active":True,
            "user_id":test_user["id"]
        },
        {
            "id": str(uuid.uuid4()),
            "title":"Job 2",
            "description":"Job 2 description",
            "location":"Job 1 location",
            "company":"Job 1 company",
            "company_url":"Job 1 company_url",
            "is_active":True,
            "user_id":test_user["id"]
        },
        {
            "id": str(uuid.uuid4()),
            "title":"Job 3",
            "description":"Job 3 description",
            "location":"Job 1 location",
            "company":"Job 1 company",
            "company_url":"Job 1 company_url",
            "is_active":True,
            "user_id":test_user["id"]
        }
    ]
    
    def create_jobs():
        for post in posts_data:
            job = Job(**post)
            session.add(job)
        session.commit()
        return session.query(Job).all()
        
    return create_jobs()
    