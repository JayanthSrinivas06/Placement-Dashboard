from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, db

router = APIRouter(
    prefix="/admins",
    tags=["admins"]
)

@router.get("/", response_model=List[schemas.AdminUser])
def get_admins(db: Session = Depends(db.get_db)):
    return db.query(models.AdminUser).all()

@router.post("/", response_model=schemas.AdminUser)
def create_admin(admin: schemas.AdminUserCreate, db: Session = Depends(db.get_db)):
    db_admin = db.query(models.AdminUser).filter(models.AdminUser.email == admin.email).first()
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_admin = models.AdminUser(
        name=admin.name,
        email=admin.email,
        password=admin.password
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

@router.put("/{id}/password")
def update_password(id: int, password_data: schemas.AdminPasswordUpdate, db: Session = Depends(db.get_db)):
    admin = db.query(models.AdminUser).filter(models.AdminUser.id == id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    admin.password = password_data.password
    db.commit()
    return {"message": "Password updated successfully"}

@router.put("/{id}", response_model=schemas.AdminUser)
def update_admin(id: int, admin_update: schemas.AdminUserBase, db: Session = Depends(db.get_db)):
    db_admin = db.query(models.AdminUser).filter(models.AdminUser.id == id).first()
    if not db_admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    db_admin.name = admin_update.name
    db_admin.email = admin_update.email
    db.commit()
    db.refresh(db_admin)
    return db_admin

@router.delete("/{id}")
def delete_admin(id: int, db: Session = Depends(db.get_db)):
    db_admin = db.query(models.AdminUser).filter(models.AdminUser.id == id).first()
    if not db_admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    db.delete(db_admin)
    db.commit()
    return {"message": "Admin deleted"}
