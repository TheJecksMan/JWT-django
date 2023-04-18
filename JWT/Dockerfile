FROM python:3.10-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt --no-cache-dir

WORKDIR /app
COPY ./JWT ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]