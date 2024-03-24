FROM python:3.12
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 9024

CMD ["python3.12", "main.py"]