FROM python:3.8-slim

COPY gpt-requirements.txt gpt-requirements.txt
COPY gpt.py gpt.py

RUN pip install -r gpt-requirements.txt

ENTRYPOINT ["python3", "csv-to-gpt.py"]