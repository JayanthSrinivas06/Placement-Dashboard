from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, db

router = APIRouter(
    prefix="/job-optins",
    tags=["job-optins"]
)

@router.post("/opt-in", response_model=schemas.JobOptIn)
def opt_in_job(optin: schemas.JobOptInCreate, db: Session = Depends(db.get_db)):
    # Check if already opted in
    existing = db.query(models.JobOptIn).filter(
        models.JobOptIn.student_id == optin.student_id,
        models.JobOptIn.job_opening_id == optin.job_opening_id
    ).first()
    
    if existing:
        if existing.status == "WITHDRAWN":
            raise HTTPException(status_code=400, detail="Cannot re-apply after withdrawing")
        raise HTTPException(status_code=400, detail="Already opted in")

    new_optin = models.JobOptIn(**optin.dict())
    db.add(new_optin)
    db.commit()
    db.refresh(new_optin)
    return new_optin

@router.post("/withdraw")
def withdraw_job(optin: schemas.JobOptInCreate, db: Session = Depends(db.get_db)):
    existing = db.query(models.JobOptIn).filter(
        models.JobOptIn.student_id == optin.student_id,
        models.JobOptIn.job_opening_id == optin.job_opening_id
    ).first()
    
    if not existing:
        raise HTTPException(status_code=404, detail="Opt-in record not found")
    
    existing.status = "WITHDRAWN"
    db.commit()
    return {"message": "Withdrawn successfully"}

@router.get("/job/{job_id}", response_model=list[schemas.JobOptIn])
def read_job_optins(job_id: int, db: Session = Depends(db.get_db)):
    optins = db.query(models.JobOptIn).filter(models.JobOptIn.job_opening_id == job_id).all()
    return optins

@router.put("/{optin_id}/status", response_model=schemas.JobOptIn)
def update_optin_status(optin_id: int, status_update: schemas.JobOptInUpdate, db: Session = Depends(db.get_db)):
    optin = db.query(models.JobOptIn).filter(models.JobOptIn.id == optin_id).first()
    if not optin:
        raise HTTPException(status_code=404, detail="Opt-in record not found")
    
    optin.status = status_update.status
    db.commit()
    db.refresh(optin)
    return optin

@router.get("/student/{student_id}", response_model=list[schemas.JobOptIn])
def read_student_optins(student_id: int, db: Session = Depends(db.get_db)):
    optins = db.query(models.JobOptIn).filter(models.JobOptIn.student_id == student_id).all()
    return optins

@router.get("/", response_model=list[schemas.JobOptIn])
def read_all_job_optins(db: Session = Depends(db.get_db)):
    return db.query(models.JobOptIn).all()

@router.delete("/{optin_id}")
def delete_job_optin(optin_id: int, db: Session = Depends(db.get_db)):
    optin = db.query(models.JobOptIn).filter(models.JobOptIn.id == optin_id).first()
    if not optin:
        raise HTTPException(status_code=404, detail="Opt-in record not found")
    
    db.delete(optin)
    db.commit()
    return {"message": "Opt-in record deleted"}
