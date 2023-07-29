FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install psycopg2
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .