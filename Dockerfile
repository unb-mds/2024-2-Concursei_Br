FROM python:3.12.3

WORKDIR /app/concursei_br/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Home.py"]