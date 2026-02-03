from flask import Blueprint, request, jsonify
from services.cases_service import (
    create_case,
    # list_cases,
    # get_case,
    # update_case,
    # delete_case,
)

cases_bp = Blueprint("cases", __name__)

@cases_bp.post("/cases")
def create_case_route():
    payload = request.get_json(silent=True) or {}
    title = (payload.get("title") or "").strip()
    case_text = (payload.get("case_text") or "").strip()

    if not title or not case_text:
        return jsonify({"error": "title and case_text are required"}), 400

    return jsonify(create_case(title, case_text))