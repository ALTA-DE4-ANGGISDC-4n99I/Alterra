# base image
FROM python:3.11.4-slim-bookworm

# aksi-aksi yang diperlukan
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# perintah yang dijalankan saat container di start
CMD uvicorn --host 0.0.0.0 main:app