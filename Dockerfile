FROM python:3.12.3-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Adds all files in the current directory to the container
COPY . /code/

CMD ["python", "src/main.py"]
