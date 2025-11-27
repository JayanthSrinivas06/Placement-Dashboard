from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, db

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)

@router.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(db.get_db)):
    total_students = db.query(models.Student).count()
    placed_students = db.query(models.Student).filter(models.Student.status == "Placed").count()
    total_jobs = db.query(models.JobOpening).count()
    total_applications = db.query(models.JobOptIn).count()

    # Application Status Breakdown
    status_counts = {}
    statuses = ["OPTED_IN", "INTERVIEW_SCHEDULED", "OFFERED", "REJECTED", "WITHDRAWN"]
    for status in statuses:
        count = db.query(models.JobOptIn).filter(models.JobOptIn.status == status).count()
        status_counts[status] = count

    return {
        "total_students": total_students,
        "placed_students": placed_students,
        "total_jobs": total_jobs,
        "total_applications": total_applications,
        "application_status_breakdown": status_counts
    }
