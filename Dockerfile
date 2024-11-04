FROM python:3.11-alpine

EXPOSE 8080/tcp
ENV token=""

WORKDIR /jsonproxy

COPY requirements.txt /jsonproxy/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /jsonproxy/requirements.txt
COPY ./app /jsonproxy/app

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]