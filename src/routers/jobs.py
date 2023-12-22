# jobs.py
from ..schemas.jobs_schemas import JobCreate, JobResponse, JobUpdate, JobInDBBase 
from ..models.jobsmodel import Job
from ..database import db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from ..controllers.job_controllers import get_jobs,post_jobs, get_single_job,update_job,delete_job
from typing import List

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/",response_model=List[JobResponse])
def read_jobs(db: Session = Depends(db.get_db)):
    return get_jobs(db)



@router.post("/", status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(db.get_db)):
    return post_jobs(job,db)


@router.get("/{job_id}",response_model=JobResponse)
def read_single_job(job_id: str, db: Session = Depends(db.get_db)):
    return get_single_job(job_id,db)


@router.patch("/{job_id}",status_code=status.HTTP_202_ACCEPTED)
def patch_job(job_id: str, jobupdate: JobUpdate, db: Session = Depends(db.get_db)):
    return update_job(job_id,jobupdate,db)


@router.delete("/{job_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_job(job_id: str, db: Session = Depends(db.get_db)):
    return delete_job(job_id,db)