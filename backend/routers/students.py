from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, db

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.get("/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(db.get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(db.get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(db.get_db)):
    db_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.put("/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(db.get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_data = student_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/{student_id}/profile", response_model=schemas.Student)
def read_student_profile(student_id: int, db: Session = Depends(db.get_db)):
    return read_student(student_id, db)

@router.put("/{student_id}/profile", response_model=schemas.Student)
def update_student_profile(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(db.get_db)):
    return update_student(student_id, student_update, db)
