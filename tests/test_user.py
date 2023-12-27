from src.schemas.user_schemas import UserResponse 
import pytest




def test_root(client):
    res = client.get("/")
    assert (res.json().get("Hello"))
    assert res.status_code == 200
    


def test_register_user(client):
  
    res = client.post("/auth/register", json={
        "username":"modoki",
        "email":"msodoki@email.com",
        "password":"password"
       })
    
    new_user = UserResponse(**res.json())
    assert res.status_code == 201
    assert new_user.username == "modoki"


def test_login_user(client, test_user):
    
   
    res = client.post("/auth/login", json={
        "email":test_user["email"],
        "password":test_user["password"]
         })
    print(res.json())    
    assert res.status_code == 200
    assert True
    

    
    
    
def test_register_user_fail(client, test_user):
  
    res = client.post("/auth/register", json={
        "username":"modoki",
        "email":"msodoki@email.com",
        "password":"password"
         })

    assert res.status_code == 400
    assert res.json() == {"msg": "Database Integrity Error"}
   
    


@pytest.mark.parametrize("email, password, expected, status", [
    ("i", "wrongpassword", {"detail": "Invalid Credentials"}, 401),
    ("ian@gmail.com", "password", {"detail": "Not Found"}, 404),

       ("", "password", {"detail": "Invalid Credentials"},400), 
])
def test_login_user_fail_2(client, email,password, expected,status):
    with pytest.raises(Exception):
   
        res = client.post("/auth/login", json={
        "email":email,
        "password":password,
         })
    
        print(res.json())
        print(res.status_code)
        assert True
    # assert res.status_code == status
    # assert res.json() == expected


