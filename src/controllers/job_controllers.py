from ..errors.notfound import NotFoundError
from sqlalchemy.orm import Session
from ..models.jobsmodel import Job

def get_jobs(db: Session ):
    return db.query(Job).all()


def post_jobs(job: Job, db: Session ):
    job = Job(**job.dict())
    db.add(job)
    db.commit()
    db.refresh(job)
    return {"message": "Job created successfully"}


def get_single_job(job_id: str, db:Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise NotFoundError("Job not found")
    return job


def update_job(job_id: str, jobupdate: Job, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise NotFoundError("Job not found")
    job.title = jobupdate.title
    job.company = jobupdate.company
    job.company_url = jobupdate.company_url
    job.location = jobupdate.location
    job.description = jobupdate.description
    job.is_active = jobupdate.is_active
    db.commit()
    db.refresh(job)
    return job



def delete_job(job_id: str, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise NotFoundError("Job not found")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}
