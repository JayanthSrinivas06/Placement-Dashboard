from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, db

router = APIRouter(
    prefix="/student-assessments",
    tags=["student-assessments"]
)

@router.post("/assign", response_model=schemas.StudentAssessment)
def assign_assessment(assignment: schemas.StudentAssessmentCreate, db: Session = Depends(db.get_db)):
    # Check if already assigned
    existing = db.query(models.StudentAssessment).filter(
        models.StudentAssessment.student_id == assignment.student_id,
        models.StudentAssessment.assessment_id == assignment.assessment_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Assessment already assigned to this student")

    new_assignment = models.StudentAssessment(**assignment.dict())
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment

@router.get("/students/{student_id}", response_model=List[schemas.StudentAssessment])
def get_student_assessments(student_id: int, db: Session = Depends(db.get_db)):
    assessments = db.query(models.StudentAssessment).filter(models.StudentAssessment.student_id == student_id).all()
    return assessments

@router.put("/{assessment_id}", response_model=schemas.StudentAssessment)
def update_student_assessment(assessment_id: int, update: schemas.StudentAssessmentUpdate, db: Session = Depends(db.get_db)):
    db_assessment = db.query(models.StudentAssessment).filter(models.StudentAssessment.id == assessment_id).first()
    if not db_assessment:
        raise HTTPException(status_code=404, detail="Assessment assignment not found")
    
    if update.status:
        db_assessment.status = update.status
    if update.score is not None:
        db_assessment.score = update.score
        
    db.commit()
    db.refresh(db_assessment)
    return db_assessment

@router.get("/", response_model=List[schemas.StudentAssessment])
def get_all_student_assessments(db: Session = Depends(db.get_db)):
    return db.query(models.StudentAssessment).all()

@router.delete("/{assessment_id}")
def delete_student_assessment(assessment_id: int, db: Session = Depends(db.get_db)):
    db_assessment = db.query(models.StudentAssessment).filter(models.StudentAssessment.id == assessment_id).first()
    if not db_assessment:
        raise HTTPException(status_code=404, detail="Assessment assignment not found")
    
    db.delete(db_assessment)
    db.commit()
    return {"message": "Assessment assignment deleted"}
