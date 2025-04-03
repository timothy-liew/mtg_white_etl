FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/

CMD ["streamlit", "run", "app/streamlit_app.py"]