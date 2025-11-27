from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, db
from .routers import auth, students, job_openings, assessments, student_assessments, job_optins, analytics, admins
import os

# Create database tables
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="Job Readiness Portal")

# CORS Setup
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500", # For local frontend testing
    "https://storied-wisp-c6f1f7.netlify.app", # Production Frontend URL
    os.getenv("FRONTEND_URL"), # Additional Production Frontend URL from env
    "*" # Allow all for development simplicity, restrict in production if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(job_openings.router)
app.include_router(assessments.router)
app.include_router(student_assessments.router)
app.include_router(job_optins.router)
app.include_router(analytics.router)
app.include_router(admins.router)

@app.on_event("startup")
def startup_event():
    db_session = db.SessionLocal()
    try:
        admin = db_session.query(models.AdminUser).filter(models.AdminUser.email == "admin@example.com").first()
        if not admin:
            default_admin = models.AdminUser(
                name="Admin",
                email="admin@example.com",
                password="admin"
            )
            db_session.add(default_admin)
            db_session.commit()
            print("Default admin created: admin@example.com / admin")
    finally:
        db_session.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Readiness Portal API"}
