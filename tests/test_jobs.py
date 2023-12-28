
import uuid

def test_get_jobs(authorized_client,test_jobs):
    res = authorized_client.get("/jobs/")
    # print(res.json())
    assert res.status_code == 200
    assert len(res.json()) == 3
    # assert res.json() == []
    
def test_unauthorized_get_jobs(client,test_jobs):
    res = client.get("/jobs/")
    assert res.status_code == 403
    assert res.json() == {"detail": "Not authenticated"}
    
    
    
def test_get_job_by_id(authorized_client,test_jobs):
    res = authorized_client.get(f"/jobs/{test_jobs[0].id}")
    assert res.status_code == 200
    assert res.json()["title"] == "Job 1"
    
def test_unauthorized_get_job_by_id(client,test_jobs):
    res = client.get(f"/jobs/{test_jobs[0].id}")
    assert res.status_code == 403
    assert res.json() == {"detail": "Not authenticated"}
    
def test_get_job_by_id_not_found(authorized_client,test_jobs):
    res = authorized_client.get(f"/jobs/{uuid.uuid4()}")
    assert res.status_code == 404
    assert res.json() == {"detail": "Job not found"}
    

def test_create_job(authorized_client,test_user):
    res = authorized_client.post("/jobs/", json={
        "title":"Job 4",
        "description":"Job 4 description",
        "location":"Job 4 location",
        "company":"Job 4 company",
        "company_url":"Job 4 company_url",
        "is_active":True,
        "user_id":test_user["id"]
    })
    print(res.json())
    assert res.status_code == 201
    assert res.json() == {"message": "Job created successfully"}
  
def test_create_job_with_invalid_data(authorized_client,test_user):
    res = authorized_client.post("/jobs/", json={
        # "title":"Job 4",
        "description":"Job 4 description",
        "location":"Job 4 location",
        "company":"Job 4 company",
        "company_url":"Job 4 company_url",
        "is_active":True,
        "user_id":test_user["id"]
    })
  
    assert res.status_code == 400
    assert res.json() == {'msg': 'Missing required fields'}


  
def test_unauthorized_create_job(client,test_user):
    res = client.post("/jobs/", json={
        "title":"Job 4",
        "description":"Job 4 description",
        "location":"Job 4 location",
        "company":"Job 4 company",
        "company_url":"Job 4 company_url",
        "is_active":True,
        "user_id":test_user["id"]
    })
    assert res.status_code == 403
    assert res.json() == {"detail": "Not authenticated"}
    
    
def test_update_job(authorized_client,test_jobs):
    res = authorized_client.patch(f"/jobs/{test_jobs[0].id}", json={
        "title":"Job 1 updated",
        "description":"Job 1 description",
        "location":"Job 1 location",
        "company":"Job 1 company",
        "company_url":"Job 1 company_url",
        "is_active":True,
        "user_id":test_jobs[0].user_id
    })
    assert res.status_code == 202
    assert res.json()["title"] == "Job 1 updated"
   
 
    
def test_unauthorized_update_job(client,test_jobs):
    res = client.patch(f"/jobs/{test_jobs[0].id}", json={
        "title":"Job 1 updated",
        "description":"Job 1 description",
        "location":"Job 1 location",
        "company":"Job 1 company",
        "company_url":"Job 1 company_url",
        "is_active":True,
        "user_id":test_jobs[0].user_id
    })
    assert res.status_code == 403
    assert res.json() == {"detail": "Not authenticated"}
    
    
    
def test_update_job_not_found(authorized_client,test_jobs):
    res = authorized_client.patch(f"/jobs/{uuid.uuid4()}", json={
        "title":"Job 1 updated",
        "description":"Job 1 description",
        "location":"Job 1 location",
        "company":"Job 1 company",
        "company_url":"Job 1 company_url",
        "is_active":True,
        "user_id":test_jobs[0].user_id
    })
    assert res.status_code == 404
    assert res.json() == {"detail": "Job not found"}
    
    
    
def test_delete_job(authorized_client,test_jobs):
    res = authorized_client.delete(f"/jobs/{test_jobs[0].id}")
    assert res.status_code == 204
  
    

def test_unauthorized_delete_job(client,test_jobs):
    res = client.delete(f"/jobs/{test_jobs[0].id}")
    assert res.status_code == 403
    assert res.json() == {"detail": "Not authenticated"}
    
    
def test_delete_job_not_found(authorized_client,test_jobs):
    res = authorized_client.delete(f"/jobs/{uuid.uuid4()}")
    assert res.status_code == 404
    assert res.json() == {"detail": "Job not found"}
    
    
    
