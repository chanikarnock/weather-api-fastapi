# setup
python -m venv .venv
source .venv/bin/activate OR . .venv/bin/activate
pip install "fastapi[standard]" uvicorn request redis
pip freeze > requirement.txt

source .venv/bin/activate OR . .venv/bin/activate
python main.py
uvicorn main:app --reload
redis-server