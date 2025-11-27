from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String) # Plain text for assignment only
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String) # Plain text for assignment only
    phone = Column(String, nullable=True)
    degree = Column(String, nullable=True)
    year_of_passout = Column(Integer, nullable=True)
    resume_url = Column(String, nullable=True)
    status = Column(String, default="Looking for job") # "Looking for job", "Placed"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    assessments = relationship("StudentAssessment", back_populates="student")
    job_optins = relationship("JobOptIn", back_populates="student")

class JobOpening(Base):
    __tablename__ = "job_openings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company_name = Column(String)
    location = Column(String)
    job_type = Column(String) # "Full-time", "Internship"
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    optins = relationship("JobOptIn", back_populates="job_opening")

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    max_score = Column(Integer)

    student_assessments = relationship("StudentAssessment", back_populates="assessment")

class StudentAssessment(Base):
    __tablename__ = "student_assessments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    assessment_id = Column(Integer, ForeignKey("assessments.id"))
    status = Column(String, default="ASSIGNED") # "ASSIGNED", "COMPLETED"
    score = Column(Integer, nullable=True)

    student = relationship("Student", back_populates="assessments")
    assessment = relationship("Assessment", back_populates="student_assessments")

class JobOptIn(Base):
    __tablename__ = "job_optins"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    job_opening_id = Column(Integer, ForeignKey("job_openings.id"))
    status = Column(String, default="OPTED_IN") # "OPTED_IN", "WITHDRAWN"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship("Student", back_populates="job_optins")
    job_opening = relationship("JobOpening", back_populates="optins")
