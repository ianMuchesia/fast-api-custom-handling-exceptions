from ..errors.notfound import NotFoundError
from sqlalchemy.orm import Session
from ..models.jobsmodel import Job

def get_jobs(db: Session, user: str ,params):
    return db.query(Job).filter(Job.title.contains(params["search"])).limit(params["limit"]).offset(params["skip"]).all()


def post_jobs(job: Job, db: Session, user: str ):
    
    job = Job(**job.dict())
    job.user_id = user
    db.add(job)
    db.commit()
    db.refresh(job)
    return {"message": "Job created successfully"}


def get_single_job(job_id: str, db:Session, user: str):
    job = db.query(Job).filter(Job.id == job_id, Job.user_id == user).first()
    if not job:
        raise NotFoundError("Job not found")
    return job


def update_job(job_id: str, jobupdate: Job, db: Session, user: str):
    job = db.query(Job).filter(Job.id == job_id,Job.user_id == user).first()
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



def delete_job(job_id: str, db: Session,user: str):
    job = db.query(Job).filter(Job.id == job_id,Job.user_id == user).first()
    if not job:
        raise NotFoundError("Job not found")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}
