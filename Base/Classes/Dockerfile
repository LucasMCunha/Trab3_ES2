FROM python:3.9-alpine

WORKDIR /Base/Classes

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ConsAlunos.py

CMD python3 ConsAlunos.py 