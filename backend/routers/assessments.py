from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, db

router = APIRouter(
    prefix="/assessments",
    tags=["assessments"]
)

@router.get("/", response_model=List[schemas.Assessment])
def read_assessments(skip: int = 0, limit: int = 100, db: Session = Depends(db.get_db)):
    assessments = db.query(models.Assessment).offset(skip).limit(limit).all()
    return assessments

@router.post("/", response_model=schemas.Assessment)
def create_assessment(assessment: schemas.AssessmentCreate, db: Session = Depends(db.get_db)):
    new_assessment = models.Assessment(**assessment.dict())
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)
    return new_assessment

@router.put("/{assessment_id}", response_model=schemas.Assessment)
def update_assessment(assessment_id: int, assessment_update: schemas.AssessmentBase, db: Session = Depends(db.get_db)):
    db_assessment = db.query(models.Assessment).filter(models.Assessment.id == assessment_id).first()
    if db_assessment is None:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    for key, value in assessment_update.dict().items():
        setattr(db_assessment, key, value)
    
    db.commit()
    db.refresh(db_assessment)
    return db_assessment

@router.delete("/{assessment_id}")
def delete_assessment(assessment_id: int, db: Session = Depends(db.get_db)):
    db_assessment = db.query(models.Assessment).filter(models.Assessment.id == assessment_id).first()
    if db_assessment is None:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    db.delete(db_assessment)
    db.commit()
    return {"message": "Assessment deleted"}
