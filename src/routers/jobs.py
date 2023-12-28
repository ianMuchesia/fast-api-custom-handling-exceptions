# jobs.py
from ..schemas.jobs_schemas import JobCreate, JobResponse, JobUpdate, JobInDBBase 

from ..database import db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from ..controllers.job_controllers import get_jobs,post_jobs, get_single_job,update_job,delete_job
from typing import List,Optional
from ..utils.ouath2 import get_current_user


router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/",response_model=List[JobResponse])
def read_jobs(db: Session = Depends(db.get_db),current_user=Depends(get_current_user), limit:int = 10, skip:int=0, search: Optional[str]=""):
    params = {"limit":limit,"skip":skip,"search":search}
    return get_jobs(db,current_user.id,params)



@router.post("/", status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(db.get_db),current_user=Depends(get_current_user)):
 
    return post_jobs(job,db,current_user.id)


@router.get("/{job_id}",response_model=JobResponse)
def read_single_job(job_id: str, db: Session = Depends(db.get_db),current_user=Depends(get_current_user)):
    return get_single_job(job_id,db,current_user.id)


@router.patch("/{job_id}",status_code=status.HTTP_202_ACCEPTED)
def patch_job(job_id: str, jobupdate: JobUpdate, db: Session = Depends(db.get_db),current_user=Depends(get_current_user)):
    return update_job(job_id,jobupdate,db,current_user.id)


@router.delete("/{job_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_job(job_id: str, db: Session = Depends(db.get_db),current_user=Depends(get_current_user)):
    return delete_job(job_id,db,current_user.id)