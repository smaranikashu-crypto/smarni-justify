import json

from db.connection import get_conn
from db.cases_sql import (
    INSERT_CASE,
    # LIST_CASES,
    # GET_CASE,
    # DELETE_CASE,
    # UPDATE_CASE_TEMPLATE,
)

from services.predict_service import predict_category

CASE_FULL_KEYS = [
    "id","created_at","title","case_text",
    "predicted_category","scores","status","notes"
]

CASE_LIST_KEYS = ["id","created_at","title","predicted_category","status"]


def create_case(title: str, case_text: str):
    category, scores = predict_category(case_text)

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                INSERT_CASE,
                (title, case_text, category, json.dumps(scores) if scores else None),
            )
            row = cur.fetchone()
        conn.commit()

    return dict(zip(CASE_FULL_KEYS, row))