from fastapi import APIRouter
import requests

router = APIRouter(prefix="/reports", tags=["Reports"])

REPORT_SERVICE = "http://localhost:8002"


@router.get("/")
def get_reports():
    response = requests.get(f"{REPORT_SERVICE}/reports")
    return response.json()


@router.post("/")
def create_report(report: dict):
    response = requests.post(f"{REPORT_SERVICE}/reports", json=report)
    return response.json()


@router.get("/{report_id}")
def get_report(report_id: int):
    response = requests.get(f"{REPORT_SERVICE}/reports/{report_id}")
    return response.json()


@router.put("/{report_id}")
def update_report(report_id: int, report: dict):
    response = requests.put(f"{REPORT_SERVICE}/reports/{report_id}", json=report)
    return response.json()


@router.delete("/{report_id}")
def delete_report(report_id: int):
    response = requests.delete(f"{REPORT_SERVICE}/reports/{report_id}")
    return response.json()