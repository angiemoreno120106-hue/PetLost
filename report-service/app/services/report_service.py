from sqlalchemy.orm import Session
from app.models.report import Report
from app.schemas.report import ReportCreate


def create_report(db: Session, report: ReportCreate):

    new_report = Report(**report.dict())

    db.add(new_report)

    db.commit()

    db.refresh(new_report)

    return new_report

def get_reports(db, pet_type=None, status=None, location=None, pet_color=None):

    query = db.query(Report)

    if pet_type:
        query = query.filter(Report.pet_type == pet_type)

    if status:
        query = query.filter(Report.status == status)

    if location:
        query = query.filter(Report.location == location)

    if pet_color:
        query = query.filter(Report.pet_color == pet_color)

    return query.all()


def get_report_by_id(db: Session, report_id: int):

    return db.query(Report).filter(Report.id == report_id).first()


def update_report(db: Session, report_id: int, report_data: ReportCreate):

    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        return None

    for key, value in report_data.dict().items():

        setattr(report, key, value)

    db.commit()

    db.refresh(report)

    return report


def delete_report(db: Session, report_id: int):

    report = db.query(Report).filter(Report.id == report_id).first()

    if not report:
        return None

    db.delete(report)

    db.commit()

    return report