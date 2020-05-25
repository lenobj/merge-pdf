# syntax=docker/dockerfile:latest

FROM python:3.8.1

LABEL NAME="Merge-PDF"
LABEL VERSION="1.0"

RUN mkdir -p /app/src && mkdir -p /app/input && mkdir mkdir -p /app/output && \
rm -rf /var/lib/apt/lists/* && apt-get clean && \
apt-get update && apt-get install --no-install-recommends -y git && \
cd /app/src && \
git clone https://github.com/lenobj/merge-pdf.git && \
python -m pip install --upgrade pip && \
cp /app/src/merge-pdf/* /app/ &&\
pip install -r /app/requirements.txt -U

WORKDIR /app

ENTRYPOINT ["python", "/app/app.py"]