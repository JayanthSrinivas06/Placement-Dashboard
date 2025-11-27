from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Admin Schemas
class AdminLogin(BaseModel):
    email: str
    password: str

class AdminUserBase(BaseModel):
    name: str
    email: str

class AdminUserCreate(AdminUserBase):
    password: str

class AdminUser(AdminUserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AdminPasswordUpdate(BaseModel):
    password: str

# Student Schemas
class StudentLogin(BaseModel):
    email: str
    password: str

class StudentBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    degree: Optional[str] = None
    year_of_passout: Optional[int] = None
    resume_url: Optional[str] = None
    status: Optional[str] = "Looking for job"

class StudentCreate(StudentBase):
    password: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    degree: Optional[str] = None
    year_of_passout: Optional[int] = None
    resume_url: Optional[str] = None
    status: Optional[str] = None
    password: Optional[str] = None

class Student(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Job Opening Schemas
class JobOpeningBase(BaseModel):
    title: str
    company_name: str
    location: str
    job_type: str
    description: str
    is_active: Optional[bool] = True

class JobOpeningCreate(JobOpeningBase):
    pass

class JobOpening(JobOpeningBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Assessment Schemas
class AssessmentBase(BaseModel):
    title: str
    description: str
    max_score: int

class AssessmentCreate(AssessmentBase):
    pass

class Assessment(AssessmentBase):
    id: int

    class Config:
        orm_mode = True

# Student Assessment Schemas
class StudentAssessmentCreate(BaseModel):
    student_id: int
    assessment_id: int

class StudentAssessment(BaseModel):
    id: int
    student_id: int
    assessment_id: int
    status: str
    score: Optional[int] = None
    assessment: Optional[Assessment] = None

    class Config:
        orm_mode = True

# Job OptIn Schemas
class JobOptInCreate(BaseModel):
    student_id: int
    job_opening_id: int

class JobOptInUpdate(BaseModel):
    status: str

class StudentAssessmentUpdate(BaseModel):
    status: str
    score: Optional[int] = None

class JobOptIn(BaseModel):
    id: int
    student_id: int
    job_opening_id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
