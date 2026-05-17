from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.database.database import SessionLocal
from app.schemas.report import ReportCreate, ReportResponse
from app.services import report_service

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ReportResponse)
def create_report(report: ReportCreate, db: Session = Depends(get_db)):
    return report_service.create_report(db, report)


@router.get("/", response_model=List[ReportResponse])
def get_reports(

    pet_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    pet_color: Optional[str] = Query(None),
    db: Session = Depends(get_db)

):

    return report_service.get_reports(db, pet_type, status, location, pet_color)


@router.get("/{report_id}", response_model=ReportResponse)
def get_report(report_id: int, db: Session = Depends(get_db)):

    report = report_service.get_report_by_id(db, report_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return report


@router.put("/{report_id}", response_model=ReportResponse)
def update_report(report_id: int, report: ReportCreate, db: Session = Depends(get_db)):

    updated = report_service.update_report(db, report_id, report)

    if not updated:
        raise HTTPException(status_code=404, detail="Report not found")

    return updated


@router.delete("/{report_id}")
def delete_report(report_id: int, db: Session = Depends(get_db)):

    deleted = report_service.delete_report(db, report_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Report not found")

    return {"message": "Report deleted"}