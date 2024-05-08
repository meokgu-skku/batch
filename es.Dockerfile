FROM python:3.8-slim

COPY es-requirements.txt es-requirements.txt
COPY restaurants.csv restaurants.csv
COPY csv-to-es.py csv-to-es.py

RUN pip install -r es-requirements.txt

ENTRYPOINT ["python3", "csv-to-es.py"]