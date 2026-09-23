Run a quick health check on Sideline OS:

1. Confirm the backend venv exists at `api/.venv`; if not, create it with `python3.12 -m venv api/.venv` and `pip install -r api/requirements.txt`.
2. Run `alembic upgrade head` in `api/` and confirm it applies cleanly.
3. Run `pytest` in `api/` and report pass/fail.
4. Run `npm run lint && npm run build && npm run test` in `web/` and report pass/fail.
5. Summarize any failures with the exact error and the file to look at first.
