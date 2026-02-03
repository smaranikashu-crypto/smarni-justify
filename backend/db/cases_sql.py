# backend/db/cases_sql.py

# ---------- INSERT ----------
INSERT_CASE = """
insert into public.cases
(title, case_text, predicted_category, scores, status, notes)
values (%s, %s, %s, %s, 'new', null)
returning id, created_at, title, case_text,
          predicted_category, scores, status, notes
"""