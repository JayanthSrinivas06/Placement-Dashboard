from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, db

router = APIRouter(
    prefix="/job-openings",
    tags=["job-openings"]
)

@router.get("/", response_model=List[schemas.JobOpening])
def read_job_openings(skip: int = 0, limit: int = 100, db: Session = Depends(db.get_db)):
    jobs = db.query(models.JobOpening).filter(models.JobOpening.is_active == True).offset(skip).limit(limit).all()
    return jobs

@router.post("/", response_model=schemas.JobOpening)
def create_job_opening(job: schemas.JobOpeningCreate, db: Session = Depends(db.get_db)):
    new_job = models.JobOpening(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.put("/{job_id}", response_model=schemas.JobOpening)
def update_job_opening(job_id: int, job_update: schemas.JobOpeningBase, db: Session = Depends(db.get_db)):
    db_job = db.query(models.JobOpening).filter(models.JobOpening.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job opening not found")
    
    for key, value in job_update.dict().items():
        setattr(db_job, key, value)
    
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
def delete_job_opening(job_id: int, db: Session = Depends(db.get_db)):
    db_job = db.query(models.JobOpening).filter(models.JobOpening.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job opening not found")
    
    db.delete(db_job)
    db.commit()
    return {"message": "Job opening deleted"}
