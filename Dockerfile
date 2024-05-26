FROM python:3.12.3-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Adds all files in the current directory to the container
COPY . /code/

ARG DISC_APP_KEY
ARG NGROK_API_KEY

ENV DISC_APP_KEY=$DISC_APP_KEY
ENV NGROK_API_KEY=$NGROK_API_KEY

CMD ["python", "src/main.py"]
