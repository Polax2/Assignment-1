FROM python:3.12.3
WORKDIR /app
COPY code/requirements.txt .
RUN pip install -r requirements.txt
COPY code/ .
EXPOSE 8050
CMD ["python", "app.py"]