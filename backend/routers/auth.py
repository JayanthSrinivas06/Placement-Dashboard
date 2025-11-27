from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/admin/login")
def admin_login(login_data: schemas.AdminLogin, db: Session = Depends(db.get_db)):
    admin = db.query(models.AdminUser).filter(models.AdminUser.email == login_data.email).first()
    if not admin:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if admin.password != login_data.password:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    return {"message": "Login successful", "user": {"id": admin.id, "name": admin.name, "email": admin.email, "role": "admin"}}

@router.post("/student/login")
def student_login(login_data: schemas.StudentLogin, db: Session = Depends(db.get_db)):
    student = db.query(models.Student).filter(models.Student.email == login_data.email).first()
    if not student:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if student.password != login_data.password:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    return {"message": "Login successful", "user": {"id": student.id, "name": student.name, "email": student.email, "role": "student"}}
